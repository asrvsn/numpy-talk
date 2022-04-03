'''
2D Lattice Kuramoto solvers using explicit fixed time-stepping
'''

import numpy as np
import numpy.typing as npt

from .base import *

# Import C++ shared object file -- this will appear in this directory at build-time
import kuramoto._cpp as _cpp

'''
Naive solver -- using for loops
'''

class NaiveSolver(KuramotoSolver):

	def dudt(self, u: npt.NDArray) -> npt.NDArray:
		''' Centered-difference gradient with zero Neumann condition '''
		dudt = self.omega.copy()

		for row in range(self.N):
			for col in range(self.N):

				# Horizontal neighbors
				if row > 0:
					dudt[row, col] += self.K * np.sin(u[row-1, col] - u[row, col])
				if row < self.N-1:
					dudt[row, col] += self.K * np.sin(u[row+1, col] - u[row, col])

				# Vertical neighbors
				if col > 0:
					dudt[row, col] += self.K * np.sin(u[row, col-1] - u[row, col])
				if col < self.N-1:
					dudt[row, col] += self.K * np.sin(u[row, col+1] - u[row, col])

		return dudt

'''
Numpy solver -- using NumPy routines
'''

class NumpySolver(KuramotoSolver):

	def dudt(self, u: npt.NDArray) -> npt.NDArray:
		dudt = self.omega.copy()

		dudx_right = u[:, 1:] - u[:, :-1]
		dudy_down = u[1:, :] - u[:-1, :]

		# Horizontal gradient
		dudt[:, :-1] += self.K * np.sin(dudx_right)
		dudt[:, 1:] += self.K * np.sin(-dudx_right)

		# Vertical gradient
		dudt[:-1, :] += self.K * np.sin(dudy_down)
		dudt[1:, :] += self.K * np.sin(-dudy_down)

		return dudt

'''
Custom C++ solver 
'''

class CppSolver(KuramotoSolver):

	def __post_init__(self):
		super().__post_init__()
		if self.dtype == np.float64:
			self._cpp_fun = _cpp.km_laplace
		elif self.dtype == np.float32:
			self._cpp_fun = _cpp.km_laplace_f32
		else:
			raise ValueError(f'dtype must either be float32 or float64, got {self.dtype}')

	def dudt(self, u: npt.NDArray) -> npt.NDArray:
		dudt = self.omega.copy()
		self._cpp_fun(u, dudt, self.K)
		return dudt

