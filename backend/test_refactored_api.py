"""Test script for the refactored API."""
import requests
import json
import time

BASE_URL = "http://127.0.0.1:8000"

def test_health():
    """Test health endpoint."""
    print("Testing health endpoint...")
    response = requests.get(f"{BASE_URL}/api/v1/health")
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    print()

def test_guidance():
    """Test guidance endpoint."""
    print("Testing guidance endpoint...")
    queries = [
        "I feel anxious and need comfort",
        "I am grateful and want to thank Allah",
        "I feel sad and depressed"
    ]
    
    for query in queries:
        print(f"\nQuery: '{query}'")
        start = time.time()
        response = requests.post(
            f"{BASE_URL}/api/v1/guidance",
            json={"emotion_query": query}
        )
        elapsed = (time.time() - start) * 1000
        
        print(f"Status: {response.status_code}")
        print(f"Response time: {elapsed:.2f}ms")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Total results: {data['total_results']}")
            for i, result in enumerate(data['results'][:3], 1):
                print(f"\n  {i}. {result['type']} - {result['citation']}")
                print(f"     Similarity: {result['similarity_score']}")
                print(f"     Translation: {result['translation'][:80]}...")
        print("-" * 80)

def test_root():
    """Test root endpoint."""
    print("Testing root endpoint...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    print()

if __name__ == "__main__":
    print("=" * 80)
    print("Islamic Guidance API - Test Suite")
    print("=" * 80)
    print()
    
    test_root()
    test_health()
    test_guidance()
    
    print("\n" + "=" * 80)
    print("All tests completed!")
    print("=" * 80)
