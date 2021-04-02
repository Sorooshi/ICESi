# ICESi methods


The source codes, experimental test-beds and, the datasets of our paper titled 
"Least-squares community extraction in feature-rich networks using similarity data"
by [Soroosh Shalileh](https://www.hse.ru/en/org/persons/316426865) and, [Boris Mirkin](https://www.hse.ru/en/staff/bmirkin), submitted to PLoS One journal.


For more information on how to call our algorithms "ICESiss", "ICESisn", "ICESins" or "ICESinn" one can 
refer to the demo jupyter notebooks "Demo_clustering_results_Lawyers". 

Also these algorithms can be run through the terminal by calling:

        python ICESiss.py/ ICESins.py/ ICESisn.py/ ICESinn.py --Name="name of dataset in data dir" --PreProcessing="z-m" --Run=1
        


  Note that the above method for calling our proposed algorithms requires the dataset to in .pickle format as it provided in data directory.  


For generating similar synthetic data sets, One should call "synthetic_data_generator.py" as 
this is demonstrated in Jupyter notebook "MediumSize_synthetic_data.ipynb".

