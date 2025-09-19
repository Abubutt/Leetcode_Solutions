class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        connected = set()
        ans = ""

        for path in paths:
            cityA, cityB = path
            connected.add(cityA)

        for path in paths:
            cityA, cityB = path
            connected.add(cityA)

            if cityB not in connected:
                return cityB