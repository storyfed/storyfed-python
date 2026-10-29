import requests
import time

class Storyfed:
    def __init__(self, api_key, base_url="https://api.storyfed.com"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json", "X-API-Key": self.api_key}

    def generate_video(self, prompt, quality_tier="Budget", ratio="9:16", estimated_length=60, poll_interval=15, verbose=True):
        """Generates the video and returns the metadata and URL."""
        payload = {"prompt": prompt, "quality_tier": quality_tier, "ratio": ratio, "estimated_length": estimated_length}
        
        if verbose:
            print("🎬 Starting Storyfed Video Generation...")
            
        res = requests.post(f"{self.base_url}/storyfed-1", headers=self.headers, json=payload)
        if res.status_code != 200: raise Exception(f"Failed to start: {res.text}")
        
        job_id = res.json().get("response", {}).get("job_id")
        
        if verbose:
            print(f"Job successfully created! ID: {job_id}")
            print(f"Polling server every {poll_interval} seconds...")
            
        last_stage = None
        
        while True:
            status_res = requests.get(f"{self.base_url}/storyfed-1/status/{job_id}", headers=self.headers)
            status_data = status_res.json()
            stage = status_data.get("stage")
            
            # Print progress ONLY when the stage changes to prevent log spam
            if verbose and stage != last_stage:
                print(f"\nCurrent Stage: {str(stage).upper()}")
                
                preview_url = status_data.get("preview_url")
                if preview_url:
                    print(f"Live Preview available at: {preview_url}")
                    
                last_stage = stage
            
            if stage == "finished" or status_data.get("status") == "completed":
                result = status_data.get("result", {})
                
                if verbose:
                    print("\nGeneration Complete!")
                    print(f"Title: {result.get('title')}")
                    print(f"Hashtags: {result.get('hashtags')}")
                    
                return result
                
            elif stage == "failed" or status_data.get("status") == "error":
                raise Exception("Generation failed on server.")
                
            time.sleep(poll_interval)

    def download(self, video_url, output_path="/tmp/video.mp4"):
        """Helper to download the MP4 for platforms like Replicate/Fal"""
        video_response = requests.get(video_url)
        with open(output_path, "wb") as file:
            file.write(video_response.content)
        return output_path
