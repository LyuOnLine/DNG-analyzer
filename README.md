DNG-analyzer
---------------
DNG file metadata inspector and analyzer.
- support subIFD structure.
- parsing and readout all tag content.
- inspect detail tag offset, value in interactive mode.

![operation](docs/operation.svg)

### usage:
- Restore python virtual environment using pipenv:

    ```
    pip3 install pipenv
    pipenv sync
    ```
  Install dependencies manually by following:
    ```
    sudo apt-get install ipython3-qtconsole
    sudo pip3 install construct
    ```
- Analyze dng file.

    ```
    $pipenv run python test/test_dng_parser.py RAW_PENTAX_K10D_SRGB.DNG       
    Loading .env environment variables…
    ================================================================
    [IFD0]
    ================================================================
    TAGS:
    subfile_type : 1 
    image_width : 160 
    image_height : 120 
    bits_per_sample : 8, 8, 8 
    compression : 1 
    photometric_interpretation : 2 
    make : PENTAX Corporation 
    model : PENTAX K10D        
    strip_offsets : 79652 
    orientation : 1 
    samples_per_pixel : 3 
    rows_per_strip : 120 
    strip_byte_counts : 57600 
    x_resolution : 72.000 
    y_resolution : 72.000 
    planar_configuration : 1 
    resolution_unit : 2 
    software : K10D Ver 1.00          
    modify_date : 2007:02:03 09:47:06
    sub_ifd : 78610, 78988 
    exif_offset : 79334 
    dng_version : 1, 1, 0, 0 
    dng_backward_version : 1, 1, 0, 0 
    unique_camera_model : PENTAX K10D
    color_matrix1 : 2.323, -0.823, -0.318, -0.459, 1.231, 0.089... 
    color_matrix2 : 1.099, -0.257, -0.038, -0.569, 1.259, 0.250... 
    ```
- Show detail metadata in interactive mode:
    - In interactive mode, IPython will be launched. 
    - All metadta in dng can be viewed with IPython TAB Completion support.
    ```
    $pipenv run python test/test_dng_parser.py -i RAW_PENTAX_K10D_SRGB.DNG
    dng analyzer started.
        dng.ifd0.TAGNAME: show detail tag info of ifd0
        dng.subifd0[0].TAGNAME: show detail tag info of subifds
    
    In [1]: dng.ifd0.color_matrix1                                                                                                                                                                                      
    Out[1]: 2.323, -0.823, -0.318, -0.459, 1.231, 0.089, -0.086, 0.168, 0.391
    ```