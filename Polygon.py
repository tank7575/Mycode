class Polygon:
        width = 0
        height = 0
        def set_values(self, width, height):
            print("^^^^ set_values")
            Polygon.width = width
            Polygon.height = height
