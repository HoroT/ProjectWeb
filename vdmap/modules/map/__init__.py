from . import cli, map, route_creator

map_ = map.Map()
cli = cli.Cli(map_)
rc = route_creator.RouteCreator()
