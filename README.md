# Personal Investment App
## Link: https://weichenghung.com

This Web-App shows some of my investment.
First of all, it uses "IEX" API and datareader to extract financial data.
Next, it analyzes data by using pandas, and store data into DataFrame.
Then, it uses plotly to plot interative chart on the web and shows some information.
It uses Flask as framework to build the web.


## Guide of Conda env
1.Create conda env
```
conda create -n stockenv
```
2.Activate env
source activate stockenv

3.Install package from requirements
conda install --yes --file requirements.txt

4.Deactivate env
source deactivate

5.Remove env
conda remove --name stockenv

6.Check conda env
conda info --envs

7.Check all package
conda list
