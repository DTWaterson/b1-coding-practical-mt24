class Controller:
    def __init__(self, kp, kd):
        self.kp = kp
        self.kd = kd
        self.previous_error = 0
    
    def get_error(self, position, target):
        
        error = position - target
        return error

    def get_action_PD(self, error, t):
        action = -(self.kp * error[t] + self.kd * (error[t] - error[t-1]))
        return action