# 🎮 3D Rendering Engine with basic Fluid Simulation

A Python-based 3D rendering engine using Pygame library, featuring a Rubik's Cube model display and trivial fluid simulation effects. 
This project was inspired by and builds upon concepts learned from [YouTube tutorial on 3D Engine and Technology of Raycasting](https://youtu.be/M_Hx0g5vFko).

## ✨ Features
_• **🖼️ 3D Object Rendering**: Loads and displays 3D models from OBJ files_

_• **🎥 Interactive Camera**: Full 360° navigation with keyboard controls_

_• **🧮 Matrix Transformations**: Support for translation, rotation, and scaling_

_• **🌊 Water Simulation**: basic fluid surface with wave animations_

## 🔧 Technical Implementation

_• **Projection Pipeline**: Implements a complete 3D rendering pipeline with perspective projection matrices_

_• **Homogeneous Coordinates**: Uses 4D homogeneous coordinates for all transforms (translation, rotation, scaling)_

_• **Camera System**: First-person camera with view matrix composition from position and orientation vectors_

_• **Object Loading**: Custom OBJ file parser that extracts vertex and face data_

_• **Wave Algorithm**: Procedural water waves using layered sine functions with time-based animation_

## 🎬 Visual Showcase

<img src="screenshots/visual_showcase.gif" alt="Start Screen" width="700"/>

## 🎮 Controls

### Camera Controls
_• **W/A/S/D**: Move camera forward/left/backward/right_

_• **Q/E**: Move camera up/down_

_• **Arrow Keys**: Rotate camera view_

## 📂 Project Structure
```
3d-engine-py/
├── main.py               # Entry point and main rendering loop
├── camera.py             # Camera implementation with movement controls
├── object_3d.py          # 3D object representation and rendering
├── projection.py         # Matrix projection utilities
├── matrix_functions.py   # Mathematical transformation functions
├── water.py              # Water surface simulation with wave effects
|
├── resources/            # Different 3d models and objects for display
|├── RubixCube.obj
|├── skull.obj
│
├── requirements.txt
└── README.md‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎# This file  
```

## 🚀 Setup and Running

## ⚙️ Installation

1. 📥 **Clone the repository:**
   ```bash
   mkdir 3d-engine-py
   cd 3d-engine-py
   git init
   # --- You May Skip first 3 commands if your directory was set
   git clone https://github.com/jafarbekyusupov/3d-engine-py.git

2. **🐍 Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv/Scripts/activate`
3. **📦 Install dependencies:**
   ```bash
   pip install -r requirements.txt # On Windows if pip is not recognized:  try py -m pip install -r requirements.txt
4. **🕹️ Run the game:**
   ```bash
   python main.py

## 🙏 Acknowledgements

> #### This project was inspired by tutorials on 3D graphics programming fundamentals available on YouTube, particularly [Creating a 3D Engine with Python by Coder Space](https://youtu.be/M_Hx0g5vFko). The core concepts were learned from these educational resources and extended with additional features like the water simulation.
