import GraphData as GD
import Grid as GRID


class GraphCollection:
    def __init__(self):
        self.graph_list = []
        self.graph_list.append(GRID.grid_gen())

    def push(self, ref_graph_data):
        self.graph_list.append(ref_graph_data)

    def get_graph_list(self):
        return self.graph_list

    def get_names(self):
        carry = []
        for ref in self.graph_list:
            carry.append(str(ref))

        return carry

    def pop(self, ref_graph_data):
        try:
            del self.graph_list[self.graph_list.index(ref_graph_data)]
            return True
        except:
            return False

    def get_element_by_index(self, index):
        return self.graph_list[index]

    def plot_by_index(self, index):
        self.graph_list[index].show()
        self.graph_list[index].plot()