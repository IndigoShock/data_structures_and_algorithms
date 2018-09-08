class Vertice:
    def __init__(self, value):
        self.value = value
        self.vertices = []

    def __repr__(self):
        pass

    def __str__(self):
        pass


class Graph:
    def __init__(self):
        self.graph = {}

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def __len__(self):
        pass

    def add_vert(self, val):
        """
        - use val to create a new Vertice.
        - Add verticeto self.graph
        - check to see if the vert already exists:
            - if so, raise exception
                - create helper method
        """

    def has_vert(self, val):
        """
        checks for a key in the graph
        """

    def add_edge(self, v1, v2, weight):
        """
        - add a relationship and weight between two verts
        - don't forget to validate
        """

    def get_neighbors(self, val):
        """
        given a val (key), return all adjacent verts
        """
