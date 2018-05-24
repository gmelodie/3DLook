class VisualizationWidget(QtWidgets.openGLWidget):
	
	def __init__(self, *args):
        super(VisualizationWidget, self).__init__(*args)
        self.element_array = None 
        self.vertex_array = None
	
	def rotate(self, theta_x, theta_y, theta_z):
		pass
		
	def translate(self, inc_x, inc_y, inc_z):
		pass
		
	def mirror(self, plane_xy, plane_yz, plane_zx):
		pass
		
	def scale(self, dx, dy, dz):
		pass

	def change_projection(self, projection_type):
		# set projection to projection_type
		pass
	
	def create_cube(self, edge):
		pass
