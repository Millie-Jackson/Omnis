# Omnis Agent Architecture

## Agent Core
- **Controller**: agent/controller.py → main decision loop
- **Planner**: agent/planning.py → decides next action
- **Memory**: agent/memory.py → access short-term and long-term memory
- **Perception**: agent/perception.py → interprets game state
- **Reflection**: agent/reflection.py → hooks into meditation/

## Meditation Module
- Runs separately or as fallback logic
- Triggered by stuck loops, goal conflict, or missing knowledge
