Link: https://weichenghung.com

This Web-App shows some of my investment.
First of all, it uses "IEX" API and datareader to extract financial data.
Next, it analyzes data by using pandas, and store data into DataFrame.
Then, it uses plotly to plot interative chart on the web and shows some information.
It uses Flask as framework to build the web.

# Create conda env
conda create -n stockenv

# Activate env
source activate stockenv

# Install package from requirements
conda install --yes --file requirements.txt

# Deactivate env
source deactivate

# Remove env
conda remove --name stockenv

# Check conda env
conda info --envs

# Check all package
conda list
