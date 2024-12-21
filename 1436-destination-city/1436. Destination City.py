class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dest = {}
        for path in paths:
            cityA, cityB = path
            dest[cityA] = cityB

        for path in paths:
            cityA, cityB = path
            if cityA not in dest:
                return cityA
            elif cityB not in dest:
                return cityB

        