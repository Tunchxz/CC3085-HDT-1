from agent import Agent
from environment import Environment

def main():
    env = Environment()
    agent = Agent()
    
    for step in range(10):
        perception = env.get_percept()
        action = agent.act(perception)
        env.update(action)
        print(f"Paso {step + 1}: Temperatura (Estado Actual)= {perception}, Acción = {action}, Nueva Temperatura = {env.get_percept()}")

if __name__ == "__main__":
    main()
