Peragro-AT
====
Peragro - Analyzers and Transcoders


http://peragro.github.io/peragro-at/


[![Build Status](https://api.travis-ci.org/peragro/peragro-at.png)](https://travis-ci.org/peragro/peragro-at)
[![Code Health](https://landscape.io/github/peragro/peragro-at/master/landscape.png)](https://landscape.io/github/peragro/peragro-at/master)
[![Coverage Status](https://coveralls.io/repos/peragro/peragro-at/badge.svg?branch=master)](https://coveralls.io/r/peragro/peragro-at?branch=master)

Installation with Docker (Recommended)
-----

**Install Docker**

Follow the [instructions](https://docs.docker.com/engine/installation/) to install docker for your system

**Now you can Pull the image from docker hub**
```
    docker pull peragro/peragro-at
```


**Or you can Build through Dockerfile**
```
    docker build -t peragro/peragro-at github.com/peragro/peragro-at
```

**For development you can rebuild just the final steps using a --build-arg**
```
    docker build -t peragro/peragro-at github.com/peragro/peragro-at --build-arg CACHEBUST=$(date +%s)
```

**Additionally you can enter the bash shell of the container using**
```
    docker run --rm -it peragro/peragro-at bash -il
```

**Run peragro-at through docker using local files**
```
    docker run --rm -v /local/path/:/peragro -it peragro/peragro-at pt a /peragro/file.blend
```

Note: You will need to replace '/local/path/' with your local path to the directory of the file as well as file.blend with the filename
	 
Installation (No Docker)
-----
Install Blender, Git, Pip and other initial python requirements 
 ```
    sudo add-apt-repository ppa:irie/blender
    sudo apt-get update -qq
    sudo apt-get install -qq blender
    sudo apt-get install -qq git
    sudo apt-get install -qq python-virtualenv
    sudo apt-get install -qq python-pip
    sudo apt-get install python-software-properties
    sudo apt-get install python-dev cython libavcodec-dev libavformat-dev libswscale-dev
    sudo apt-get install python-pyassimp
    sudo apt-get install sox libsox-fmt-mp3
    sudo apt-get install ffmpeg
    sudo apt-get build-dep python-matplotlib
    sudo apt-get install python3-dev
    sudo apt-get install python3-setuptools
    sudo apt-get install libassimp-dev
 ```

Install Thrift globally for python3
 ```
    git clone -b 0.10.0 https://github.com/apache/thrift.git
    cd thrift/lib/py
    python3 setup.py install
    cd ../../..
 ```
 
 Install matplotlib and pyassimp
```
    pip install matplotlib
    pip install pyassimp
```

 Checkout peragro-at
 ```
    git clone https://github.com/peragro/peragro-at.git
 ```
  
 Install peragro-at
 ```
    cd peragro-at
    sudo python3 setup.py develop
    cd ..
 ```

Optional: checkout test files
 ```
    git clone https://github.com/peragro/peragro-test-files.git
 ```
 Optional: install autocomplete
 ```
    eval "$(register-python-argcomplete pt)"
 ```

Windows: install assimp dll
 ```
    download https://superb-dca2.dl.sourceforge.net/project/assimp/assimp-3.1/assimp-3.1.1-win-binaries.zip
	grab dll from bin32 or bin64 depending on python version
    Put assimp.dll into C:\Python351\lib\site-packages\pyassimp\
 ```
 
Usage
-----
Analyze
 ```
    pt a peragro-test-files/mesh/blender/cube1.blend --store /tmp/peragro
 ```
  Output:
 ```
    ----------------------------------------------------------------------
    Analyzing peragro-test-files/mesh/blender/cube1.blend into /tmp/peragro
    ----------------------------------------------------------------------

    52c676b407d05d50282661b7b451a52cc93b46d2
    ----------------------------------------
    Assets: 5
      -->Cube1-data  (application/x-blender.mesh)
      -->Camera  (application/x-blender.object)
      -->Cube1-object  (application/x-blender.object)
      -->Lamp  (application/x-blender.object)
      -->Text  (application/x-blender.text)
 ```

Inspect
 ```
    pt i /tmp/peragro/90/ca0b2230d6f9b486cd932e1ae1c28b780a2b0c
 ```
  Output:
 ```
    Inspecting "/tmp/peragro/52c676b407d05d50282661b7b451a52cc93b46d2"

    hash: 52c676b407d05d50282661b7b451a52cc93b46d2
    filename: /home/sueastside/peragro-test-files/mesh/blender/cube1.blend
    5 Assets:
    ================================================================================
    * Cube1-data (application/x-blender.mesh)
      hash: 52c676b407d05d50282661b7b451a52cc93b46d2
      filename: /home/sueastside/peragro-test-files/mesh/blender/cube1.blend
      Dependencies (1):
        * crate10b.jpg (image/jpeg)
          hash: 8c8065ae5590cb5d669426651ce229ed11c5f07d
          filename: ../../image/jpg/crate10b.jpg
      MetaData (2):
        * nr_of_vertices: 24
        * nr_of_faces: 0
    --------------------------------------------------------------------------------
    * Camera (application/x-blender.object)
      hash: 52c676b407d05d50282661b7b451a52cc93b46d2
      filename: /home/sueastside/peragro-test-files/mesh/blender/cube1.blend
    --------------------------------------------------------------------------------
    * Cube1-object (application/x-blender.object)
      hash: 52c676b407d05d50282661b7b451a52cc93b46d2
      filename: /home/sueastside/dev/peragro-test-files/mesh/blender/cube1.blend
      Dependencies (1):
        * Cube1-data (application/x-blender.mesh)
          hash: 52c676b407d05d50282661b7b451a52cc93b46d2
          filename: /home/sueastside/peragro-test-files/mesh/blender/cube1.blend
    --------------------------------------------------------------------------------
    * Lamp (application/x-blender.object)
      hash: 52c676b407d05d50282661b7b451a52cc93b46d2
      filename: /home/sueastside/peragro-test-files/mesh/blender/cube1.blend
    --------------------------------------------------------------------------------
    * Text (application/x-blender.text)
      hash: 52c676b407d05d50282661b7b451a52cc93b46d2
      filename: /home/sueastside/peragro-test-files/mesh/blender/cube1.blend
    --------------------------------------------------------------------------------
 ```

Transcode
 ```
    pt -v t peragro-test-files/image/png/b2csmaterialpanel.png  "Cube1-data(application/x-blender.mesh)" "image/png" -h
 ```
  Output:
 ```
    usage: pt transcode [-h] [--size SIZE] [--quality QUALITY]

    optional arguments:
      -h, --help         show this help message and exit
      --size SIZE        The target size of the image (Value needs to be between 1
                         and 4096) [default: (-1, -1)]
      --quality QUALITY  The target quality of the image (Value needs to be
                         between 0.0 and 1.0) [default: 1.0]
 ```

Or
 ```
    pt -v t peragro-test-files/mesh/blender/cube1.blend  "Cube1-data(application/x-blender.mesh)" "image/png" -h
 ```
  Output:
 ```
    usage: pt transcode [-h] [--size SIZE] [--camera_type CAMERA_TYPE]
                             [--angles ANGLES]

    optional arguments:
      -h, --help            show this help message and exit
      --size SIZE           The target size of the image (Value needs to be
                            between 1 and 4096) [default: (64, 64)]
      --camera_type CAMERA_TYPE
                            The camera type (Value needs to be one of ('ORTHO',
                            'PERSPECTIVE')) [default: PERSPECTIVE]
      --angles ANGLES       The angle (Value needs to be between 0.0 and 3.1415)
                            [default: (0.0,)]
 ```

And finally lets generate a thumb for a blender mesh datablock
 ```
    pt -v t peragro-test-files/mesh/blender/cube1.blend  "Cube1-data(application/x-blender.mesh)" "image/png" --size=64,64
 ```
  Output:
 ```
    Transcoding "/home/sueastside/peragro-test-files/mesh/blender/cube1.blend"

    Using: Blender object render transcoder
    with:
    * camera_type: PERSPECTIVE
    * angles: (0.0,)
    * size: [64, 64]
    0
    ['assets/NoneCube1-dataapplication__x-blender.mesh/image/png/[64, 64]/PERSPECTIVE/0.0/NoneCube1-dataapplication__x-blender.mesh.png']
 ```

 ```
    eog /tmp/transcoded/assets/NoneCube1-dataapplication__x-blender.mesh/image/png/\[64\,\ 64\]/PERSPECTIVE/0.0/NoneCube1-dataapplication__x-blender.mesh.png
 ```
