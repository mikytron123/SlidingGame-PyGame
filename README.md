
<h3 align="center">Sliding Game</h3>
  <p align="center">
    Sliding Torus number puzzle game created with pygame 
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Sliding Game Screen Shot][product-screenshot]]

This project is built using numpy and Pygame. Numpy is used for storing internal state. 

An autosolver algorithm is also implmented using solution from [How to Solve the Torus Puzzle](https://www.researchgate.net/publication/220654877_How_to_Solve_the_Torus_Puzzle)


### Built With

* [![Pygame.org]][Pygame-url]
* [![Numpy.org]][Numpy-url]



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

## Prerequisites

* python
  ```sh
  pip install -r requirements.txt
  ```

<!-- USAGE EXAMPLES -->
## Usage

```python
python sliding.py
```
A grid size must be entered before starting the game. 

The autosolver can be invoked using the 's' key


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: ./Images/screenshot.png
[Pygame-url]:https://www.pygame.org
[Pygame.org]:https://img.shields.io/badge/Pygame-black?style=for-the-badge&logo=python&logoColor=3776AB
[Numpy-url]:https://numpy.org/
[Numpy.org]:https://img.shields.io/badge/Numpy-black?style=for-the-badge&logo=Numpy&logoColor=013243
