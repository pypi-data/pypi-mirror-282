import hashlib
import json
from time import sleep
from typing import List
from upstash_vector import Index
from dotenv import load_dotenv
import os
from langchain.globals import set_llm_cache
from langchain_openai import OpenAI
from langchain_core.outputs.generation import Generation
import time

class SemanticCache:    
    def __init__(self, url, token, min_proximity: float = 0.9):
        self.min_proximity = min_proximity
        self.index = Index(url=url, token=token)

    # searches the cache for the key and returns the value if it exists
    def get(self, key):
        response = self.query_key(key)
        if response is None or response.score <= self.min_proximity:
            return None
        return response.metadata['data']
    
    # langchain specific function
    # converts the json string to generations and returns  
    def lookup(self, prompt, llm_string : str = None):
        result = self.get(prompt)
        return self._loads_generations(result) if result else None
    
    # another langchain specific function
    # converts the generations to a json string and stores it in the cache     
    def update(self, prompt,  llm_string : str = None, result : str = None):
        self.set(prompt, self._dumps_generations(result))

    # queries the cache for the key
    def query_key(self, key):
        response = self.index.query(
            data=key,
            top_k=1,
            include_metadata=True
        )
        return response[0] if response else None

    # sets the key and value in the cache
    def set(self, key, data):
        if (type(key) == list) and (type(data) == list):
            for i in range(len(key)):
                self.index.upsert([(self._hash_key(key[i]), key[i], {'data': data[i]})])
        else:
            self.index.upsert([(self._hash_key(key), key, {'data' : data})])

    def delete(self, key):
        self.index.delete([self._hash_key(key)])
        
    def bulk_delete(self, keys: List[str]):
        for key in keys:
            self.delete(key)
        
    def flush(self):
        self.index.reset()

    # helper functions
    def is_2d_list(self, lst):
        return isinstance(lst, list) and all(isinstance(sublist, list) for sublist in lst)
    
    # converts the generations to a json string
    def _dumps_generations(self, generations):
        def generation_to_dict(generation):
            if isinstance(generation, Generation):
                return {
                    "text": generation.text,
                    "generation_info": generation.generation_info
                }
            else:
                raise TypeError(f"Object of type {generation.__class__.__name__} is not JSON serializable")
        return json.dumps([generation_to_dict(g) for g in generations])

    # converts the json string to generations
    def _loads_generations(self, json_str):
        def dict_to_generation(d):
            if isinstance(d, dict):
                return Generation(text=d["text"], generation_info=d["generation_info"])
            else:
                raise TypeError(f"Object of type {d.__class__.__name__} is not a valid Generation dict")

        return [dict_to_generation(d) for d in json.loads(json_str)]
    
    # hashes the key to generate id
    def _hash_key(self, key):
        return hashlib.sha256(key.encode('utf-8')).hexdigest()

def example1(llm):
    prompt1 = "Why is the Moon always showing the same side?"
    prompt2 = "How come we always see one face of the moon?"

    start_time = time.time()
    response1 = llm.invoke(prompt1)
    print(response1)
    end_time = time.time()
    print("Time difference 1:", end_time - start_time, "seconds")
    sleep(1)
    
    start_time = time.time()
    response2 = llm.invoke(prompt2)
    print(response2)
    end_time = time.time()
    time_difference = end_time - start_time
    print("Time difference 2:", time_difference, "seconds")
    

def main():
    # set environment variables
    load_dotenv()
    UPSTASH_VECTOR_REST_URL = os.getenv('UPSTASH_VECTOR_REST_URL')
    UPSTASH_VECTOR_REST_TOKEN = os.getenv('UPSTASH_VECTOR_REST_TOKEN')

    # create a cache object
    cache = SemanticCache(url=UPSTASH_VECTOR_REST_URL, token=UPSTASH_VECTOR_REST_TOKEN, min_proximity=0.7)
    cache.flush()
    sleep(1)
    
    llm = OpenAI(model_name="gpt-3.5-turbo-instruct", n=2, best_of=2)
    set_llm_cache(cache)
    example1(llm)
    
if __name__ == '__main__':
    main()

