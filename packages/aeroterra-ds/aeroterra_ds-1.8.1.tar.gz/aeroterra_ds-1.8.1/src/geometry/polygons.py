import geopandas as gpd

from rtree import index

from shapely import unary_union

from shapely.geometry import Polygon, MultiPolygon


def get_intersections(polygons, precise=True):
    """
    Given a list of polygons it returns the positions of those that intersect each other

    Parameters:
        - polygons: List of polygons to check
        - precise: If intersection must be secured or if it could use rtree one
    
    Returns a dictionary with List positions as key and a list of other positions intersecting
    as value
    """
    idx = index.Index()
    intersected_polygons = {}

    for i, polygon in enumerate(polygons):
        idx.insert(i, polygon.bounds)
        intersected_polygons[i] = []

    for i, polygon1 in enumerate(polygons):
        intersections = []
        for j in idx.intersection(polygon1.bounds):
            if j <= i:
                continue
            if precise or polygon1.intersects(polygons[j]):
                intersections.append(j)
                intersected_polygons[j].append(i)
        intersected_polygons[i].extend(intersections)
    
    return intersected_polygons


def create_unique_lists(intersections):
    """
    Given a dictionary of intersections it returns the unique list of joined elements

    Parameters:
        - intersections: Dict of intersections. Key: Position of element, Value: List of intersections
    """
    visited = set()
    unique_links = []

    def dfs(node, current_link):
        visited.add(node)
        current_link.append(node)

        for neighbor in intersections.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, current_link)

    for key in intersections.keys():
        if key not in visited:
            current_link = []
            dfs(key, current_link)
            unique_links.append(current_link)
    
    return unique_links


def join_by_intersections(polygons, values_column, precise=True):
    """
    Given a GeoDataFrame with polygons, it returns new GeoDataFrame with the set
    of intersected polygons joined.

    Parameters:
        - polygons: GeoDataFrame to join
        - values_column: Dictionary indicating new columns to create with operations
            to do with the combination.
                {new_key: [operation_type, operation_column]}
                operation_types:
                    - sum
                    - count
                    - unique
                    - max
                    - min
        - precise: If intersection must be secured or if it could use rtree one
    """
    geometry_column = polygons.geometry.name
    crs = polygons.crs
    pols_list = polygons[geometry_column].to_list()
    intersections = get_intersections(pols_list, precise=precise)
    links = create_unique_lists(intersections)
    
    polygons_final = []
    
    for link in links:
        if len(link) == 0:
            continue
        polygons_current = [pols_list[i] for i in link]
        polygon = unary_union(polygons_current[geometry_column].to_list())
        if isinstance(polygon, Polygon):
            polygon = MultiPolygon([polygon])
        
        values = {geometry_column: polygon}
        for new_key, operation in values_column.items():
            metric = None
            operation_key = operation[0]
            operation_action = operation[1]
            if operation_action == "sum":
                metric = polygons_current[operation_key].sum()
            elif operation_action == "count":
                metric = polygons_current[operation_key].count()
            elif operation_action == "unique":
                metric = len(polygons_current[operation_key].unique())
            elif operation_action == "max":
                metric = polygons_current[operation_key].max()
            elif operation_action == "min":
                metric = polygons_current[operation_key].min()
            values[new_key] = metric

        polygons_final.append(values)

    return gpd.GeoDataFrame(polygons, geometry=geometry_column, crs=crs)
