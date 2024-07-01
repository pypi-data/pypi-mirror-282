from gemini_application.application_abstract import ApplicationAbstract
import numpy as np
from matplotlib import pyplot as plt


class InjectionWellMonitoring(ApplicationAbstract):
    """Class for application injection well II (Injectivity Index) & BHP calculations"""

    def __init__(self):
        super().__init__()

    def init_parameters(self):
        """Function to initialize model parameters"""
        pass

    def calculate(self):
        """Function to calcaulte hall integral"""
        self.get_data()
        self.calculate_hall_integral()

    def get_data(self):
        start_time = self.inputs['start_time']
        end_time = self.inputs['end_time']
        timestep = 3600  # hardcoded 1 hour since flowrate is in m3/h

        database = self.plant.databases[0]

        result, time = database.read_internal_database(
            self.unit.plant.name,
            self.unit.name,
            'injectionwell_flow.measured',
            start_time,
            end_time,
            str(timestep) + 's'
        )
        self.inputs['flow'] = np.array(result)

        result, time = database.read_internal_database(
            self.unit.plant.name,
            self.unit.name,
            'injectionwell_bottomhole_pressure.calculated',
            start_time,
            end_time,
            str(timestep) + 's'
        )
        self.inputs['BHP'] = np.array(result)

    def calculate_hall_integral(self):
        """Function to calculate hall integral and its derivative"""
        cumulative_production = self.inputs['flow'].cumsum()
        hall_integral = (self.inputs['BHP'] - self.inputs['reservoir_pressure']).cumsum()
        hall_derivative_numerical = np.gradient(hall_integral, np.log(cumulative_production))

        self.outputs['cumulative_flow'] = cumulative_production
        self.outputs['hall_integral'] = hall_integral
        self.outputs['hall_derivative_numerical'] = hall_derivative_numerical

    def plot(self):
        """Function to calculate all pressure from reservoir to topside"""
        x = self.outputs['cumulative_flow']
        y0 = self.outputs['hall_integral']
        y1 = self.outputs['hall_derivative_numerical']

        plt.figure()
        plt.plot(x, y0, label='hall_integral')
        plt.plot(x, y1, label='hall_derivative_numerical')
        plt.legend()
        plt.show()

        plt.figure()
        plt.plot(x, y0, label='hall_integral')
        plt.plot(x, y1, label='hall_derivative_numerical')
        plt.xscale('log')
        plt.yscale('log')
        plt.legend()
        plt.show()
