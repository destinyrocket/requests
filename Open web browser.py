Basic open web browser
first import the module
import webbrowser
  
# then make a url variable
url = "https://www.geeksforgeeks.org"
  
# then call the default open method described above
webbrowser.open(url)
---------------------------------------------------------

Specify the browser
import webbrowser
  
# then make a url variable
url = "https://www.geeksforgeeks.org"
  
# then call the get method to select the code 
# for new browser and call open method 
# described above
webbrowser.get('chrome').open(url)
 results in error since chrome is not registered initially.
---------------------------------------------------------
Register the browser
# first import the module
import webbrowser
  
# then make a url variable
url = "https://www.geeksforgeeks.org"
  
# getting path
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
  
# First registers the new browser
webbrowser.register('chrome', None, 
                    webbrowser.BackgroundBrowser(chrome_path))
  
# after registering we can open it by getting its code.
webbrowser.get('chrome').open(url)
