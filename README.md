# DoubleB Commisioning 

More information the [twiki](https://twiki.cern.ch/twiki/bin/viewauth/CMS/DoubleBTagCommissioning)

To download this repo, it is recommended to clone it under `RecoBTag/PerformanceMeasurements/test` but not needed:
~~~
git clone -b 9_4_X https://github.com/cms-btv-pog/DoubleBCommissioning.git
~~~

There are several files from previous iterations. However the simplest way to submit jobs is through the `multicrab.py` script, for instance:
~~~
python multicrab.py -d BTag -s T3_US_FNALLPC -v 9_4_X_v1
~~~
there: 
 * `-d` specifies the dataset stored [here](https://github.com/alefisico/DoubleBCommissioning/blob/9_4_X/multicrab.py#L54-L65). To send all the data jobs, just include: `-d BTagMu`. To send all the QCD jobs: `-d QCD`. Or to send QCD and data: `-d all`
 * `-s` specifies the storage site.

By default, the jobs will be stored in your EOS area under: `/store/user/YOURUSERNAME/DoubleBTagCOmmissioning/VERSION`
