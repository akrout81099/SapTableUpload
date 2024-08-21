# SapTableUpload
Python Program to upload data from SAP To Target

## Prequisite:
* [Python 12](https://www.python.org/downloads/) or higher needs to be installed
* Set up SAPNWRFC_HOME environment
  * #### Windows
    * Download [nwrfcsdk](https://support.sap.com/en/product/connectors/nwrfcsdk.html) from SAP website
    * Extract the downloaded zip file into C drive and rename the folder to **nwrfcsdk**
      <img height="250" src="readmeimages\image_nwrfcsdk_1.png" width="600"/>
      
      * <span style="color:red">**Note: In this example we have saved the content in C drive in folder 
        called SAP_NET_WEAVER**</span>
    * Open Start Menu and open **Edit the system environment variables**
    
      <img alt="Edit the system environment variables" width ="600" height="165" src="readmeimages/image_nwrfcsdk_2.png"/>
      
      <img alt="Edit the system environment variables" width ="400" height="408" src="readmeimages/image_nwrfcsdk_3.png"/>
    * Click on **Environment Variables** at the right bottom
    
      <img alt="Edit the system environment variables" width ="400" height="440" src="readmeimages/image_nwrfcsdk_4.png"/>
    * Click on **New** button under **User Variables** and add SAPNWRFC_HOME as name and the path to **nwrfcsdk** in
      the path and then press **OK** button 
    
      <img alt="Edit the system environment variables" width ="400" height="120" src="readmeimages/image_nwrfcsdk_5.png"/>
    * Under **System Variables** look for an entry name **Path**
      
      <img alt="Edit the system environment variables" width ="400" height="180" src="readmeimages/image_nwrfcsdk_6.png"/>
    * Click **Edit..** button

      <img alt="Edit the system environment variables" height="450" src="readmeimages/image_nwrfcsdk_7.png"/>
    * Click on **New** button and add the path to **bin** folder inside **nwrfcsdk** and then click on
      **New** button again and add the path **nwrfcsdk** folder
      
      <img alt="Edit the system environment variables" height="500" src="readmeimages/image_nwrfcsdk_8.png"/>
    * Click **OK** button in all the windows open
    
    


