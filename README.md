# Mildew Detector


## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

### What is powdery mildew?

According to [RHS](https://www.rhs.org.uk/disease/powdery-mildews), Powdery mildew is a fungal disease of the foliage, stems and occasionally flowers and fruit where a superficial fungal growth covers the surface of the plant.

Many common edible and ornamental garden plants are affected including apples, blackcurrants, gooseberries, grapes, crucifers, courgettes, marrows, cucumbers, peas, grasses (the powdery mildew fungi are major pathogens of cereal crops), Acanthus, delphiniums, phlox, many ornamentals in the daisy family, Lonicera (honeysuckle), rhododendrons and azaleas, roses and Quercus robur (English oak).

Powdery mildews usually have narrow host ranges comprising of just a few related plants. For example, the powdery mildew affecting peas is a different species from the one attacking apples.

## Hypothesis and how to validate?
 I suspect that leaves affected by powdery mildew will show clear marks/signs. Typically, leaves infected with mildew will have clear powdery patches of fungus, thereby making the leaves appear as if they have been dusted with flour. Whereas healthy leaves will be light green in colour.
    * An average image study will help validate this hypothesis.


## The rationale to map the business requirements to the Data Visualisations and ML tasks
#### Business Requirement 1: Data Visualisations
* I want to display the mean and standard deviation images for cherry leaves that are affected by mildew and those that are healthy, so that I can visually differentiate them.
* I want to display the difference between an average infected leaf and an average uninfected leaf.
* I want to display an image montage for either infected, or uninfected leaves.

#### Business Requirement 2: ML Tasks (Classification)
* I want to predict if a given leaf is infected with mildew or is healthy.
* I want to build an ML model that works as a binary classifier, and generate reports.

## ML Business Case

### MildewClf
* We want an ML model to predict if a leaf shows signs/marks of mildew or not, based on historical image data. It is a supervised model, a 2-class, single-label, classification model.
* Our ideal outcome is to provide the employes of Farmy & Foods a faster and more reliable diagnostic for powdery mildew detection.
* The model success metrics are
	* Accuracy of 99% or more on the test set.
* The model output is defined as a flag, indicating if the leaf shows powdery mildew or not and the associated probability of being infected or not. The employees will take pictures of cherry leaves and upload the pictures to the App. The prediction is made on the fly (not in batches).
* Heuristics: The current procedure requires an experienced employee to carry out a time-consuming manual process inspection to distinguish infected and uninfected leaves. Visual criteria are used to detect mildew fungus. It leaves room to produce inaccurate diagnostics due to human error. On top of that, it will save the employess of Farmy & Foods a great amount of time by eliminating the need for manual process inspection. Rather, a picture of the leaf is taken and uploaded to the App and the App distinguishes between infected and uninfected leaves. 
* The training data to fit the model come from the dataset provided by the Code Institute and saved to this [Kaggle dataset directory](https://www.kaggle.com/codeinstitute/cherry-leaves). This dataset contains 4208 images for quicker model training.
	* Train data - target: infected or not; features: all images

## Agile Methodology and CRISP-DM Workflow

THe agile methodolody and CRISP-DM workflow were used in planning and developing this project.

The CRISP-DM workflow was used to delve deeper into the business requirements of the client and improve our compliance with business understanding. That and the further steps of data understanding and preparation, modelling, evaluation and deplyment; were broken down into milestones on Github projects. Issues related to the project development and business requirements were then assigned to fdacilitate the relevant milestone.

Please view the Github projects board [here](https://github.com/users/StephenB92/projects/5/views/1).


## Dashboard Design


## Fixed Bugs


## Deployment


### Heroku

* The App live link is: 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.


## Main Data Analysis and Machine Learning Libraries


## Credits 
* Credit to [RHS](https://www.rhs.org.uk/disease/powdery-mildews) and [Almanac](https://www.almanac.com/pest/powdery-mildew) for information on powdery mildew and how to identify it.
* Credit to Code Institute's [Malaria Detector Walkthrough Project](https://learn.codeinstitute.net/courses/course-v1:code_institute+CI_DA_ML+2021_Q4/courseware/07a3964f7a72407ea3e073542a2955bd/29ae4b4c67ed45a8a97bb9f4dcfa714b/), which was used as a guide during development of this project.

### Content 


### Media



## Acknowledgements

