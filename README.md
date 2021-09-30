# Splash Screen Python
[![NPM](https://img.shields.io/github/license/Robsonmxms/splash_screen_python)](https://github.com/Robsonmxms/splash_screen_python/blob/master/LICENSE)

# About Project
Splash screen model for Python applications using PySide2

## The Application

In the [main.py](https://github.com/Robsonmxms/splash_screen_python/blob/master/main.py) you can: 

- set the title and credits in the interface function:

```python
def interface(self):
    self.setTitle("<strong>YOUR</strong> APPLICATION")
    self.setCredits("<strong>Created by:</strong> Robson L. Lopes")
    self.__removeTitleBar()
    self.__dropShadowEffect()
    self.__startQTimerInMilliseconds()
    self.__changeDescription()
    self.show()
```

- change descriptions, in the __changeDescription function:

```python
def __changeDescription(self):
    QtCore.QTimer.singleShot(
        0,
        lambda: self.ui.label_description
        .setText("<strong>LOADING</strong> DATABASE")
    )
    QtCore.QTimer.singleShot(
        4000, 
        lambda: self.ui.label_description
        .setText("<strong>LOADING</strong> DATABASE")
    )
    QtCore.QTimer.singleShot(
        8000, 
        lambda: self.ui.label_description
        .setText("<strong>LOADING</strong> USER INTERFACE")
    )
```

- Result:

![splash_screen](https://github.com/Robsonmxms/splash_screen_python/blob/master/assets/images/splash_screen.PNG)

# How to Run the Project
- At work terminal:
  
  ```bash

  # Clone repository
  git clone https://github.com/Robsonmxms/splash_screen_python.git

  # Get Requirements
  pip install -r requirements.txt

  ```
- Create a shortcut as "Qt Designer" to the following file:

      C:\Users\robso\AppData\Local\Programs\Python\Python39\Lib\site-packages\PySide2\designer.exe

- Edit [Main UI](https://github.com/Robsonmxms/splash_screen_python/blob/master/ui/main.ui) in the Qt Designer

- At work terminal:

  ```bash

  #Convert ui to py
  pyside2-uic C:\Users\robso\Desktop\splash_screen_python\ui\main.ui -o ui_main.py - x

  ```
  + If you use a resource file, example:
    ```bash
    
    #Convert qrc to py
    pyside2-rcc C:\Users\robso\Desktop\splash_screen_python\assets\resource.qrc -o resource_rc.py
    
    ```
- Edit your application in the class [MainWindow](https://github.com/Robsonmxms/splash_screen_python/blob/master/main.py) 
