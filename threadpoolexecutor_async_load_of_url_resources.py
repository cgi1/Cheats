from concurrent.futures import ThreadPoolExecutor

class AsyncThreadPoolGetter():

  def ___init___(self):
    self.loaded_data = pd.DataFrame()

  def request_from_url(self, url)
      print("Do your request here and save the results to a class variable using self.loaded_data")

  def run_urls(self, urls)
    
    with ThreadPoolExecutor(max_workers=max_threads) as executor:

        futures_to_todo = []
        for url in urls:
            futures_to_todo.append(executor.submit(fn=request_from_url, url=url))

        wait(futures_to_todo)
        print("Finished async job. Access self.loaded_data now")

