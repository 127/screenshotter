# Basic python utility to optimize emulator screenshots for App Store and Google Play

## Installation 
- Install python3
- Install Pillow lib with ```pip install pillow```

# Demo 
- Run the script with ```python screens.py``` and take a look at ```results``` folder

## Usage 

- Change paths with variables at screens.py
```
sources_dir = "test/sources"
results_dir = "test/results"
\# background for padded areas
bg_path = 'test/bg1.jpg'
```
- change default array of resolutions (current is the minimal to pass to Play & App Stores)
```

resolutions =  { "iphone": [
                    (2778, 1284), (2208, 1242)
                  ],
                  "ipad":  [
                    (2732, 2048)
                  ] 
                }
```

- Run the script with ```python screens.py```
- Get results in ```{results_dir}```