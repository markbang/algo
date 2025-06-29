"""
This script processes a JSON file containing image evaluations.
For each image, it fetches the original_path using a curl-like command
and constructs a full image URL, then saves the updated data to a new JSON file.
"""

import json
import asyncio  # Added asyncio
import httpx  # Added httpx
# For more robust HTTP requests, consider using the `requests` library:
# import requests # You might need to install it: pip install requests


async def get_original_path(
    client: httpx.AsyncClient, image_id: str
) -> str | None:  # Modified to be async and take client
    """
    Fetches the original_path for a given image_id using httpx.

    Args:
        client: An httpx.AsyncClient instance.
        image_id: The ID of the image.

    Returns:
        The original_path if found, otherwise None.
    """
    bearer_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiaW1hZ2VkYXRhYmFzZV9wb3N0Z3Jlc3QifQ.XypL-YQyvu4yEeZL8CfogHXsdUHHkdGmQTuaRGJ2zDA"
    url = (
        f"https://imgrest.talesofai.cn/artifacts?id=eq.{image_id}&select=original_path"
    )
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {bearer_token}",  # Corrected f-string usage
    }

    try:
        response = await client.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)

        response_json = response.json()

        if response_json and isinstance(response_json, list) and len(response_json) > 0:
            if "original_path" in response_json[0]:
                return response_json[0]["original_path"]
            else:
                print(
                    f"Warning: 'original_path' not found in response for image_id {image_id}. Response: {response.text}"
                )
                return None
        else:
            print(
                f"Warning: Unexpected response structure for image_id {image_id}. Response: {response.text}"
            )
            return None

    except httpx.HTTPStatusError as e:
        print(
            f"HTTP error occurred for image_id {image_id}: {e.response.status_code} - {e.response.text}"
        )
        print(f"URL: {url}")
        return None
    except httpx.RequestError as e:
        print(f"Request error occurred for image_id {image_id}: {e}")
        print(f"URL: {url}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response for image_id {image_id}: {e}")
        print(
            f"Response text: {response.text}"
        )  # Ensure response is defined in this scope
        return None
    except Exception as e:
        print(
            f"An unexpected error occurred while fetching original_path for image_id {image_id}: {e}"
        )
        return None


async def process_json_file(
    input_path: str, output_path: str, url_prefix: str
):  # Modified to be async
    """
    Reads a JSON file, processes each item to add an image_url asynchronously,
    and writes the result to a new JSON file.
    """
    updated_data = []

    try:
        print(f"Attempting to load JSON data from {input_path}...")
        with open(input_path, "r", encoding="utf-8") as infile:
            data = json.load(infile)

        if not isinstance(data, list):
            print("Error: Expected a JSON array in the input file.")
            return

        total_items = len(data)
        print(f"Successfully loaded {total_items} items.")

        tasks = []  # Moved tasks list initialization here
        async with httpx.AsyncClient() as client:  # Create an AsyncClient session
            for i, item in enumerate(data):
                if isinstance(item, dict) and "image_id" in item:
                    image_id = item["image_id"]
                    # Create a task for each image_id
                    tasks.append(get_original_path(client, image_id))
                else:
                    # For items not matching the structure, we'll append a future that resolves to None.
                    # This keeps the task list aligned with the data list.
                    future = asyncio.Future()
                    future.set_result(None)
                    tasks.append(future)

            print(f"Fetching original_paths for {total_items} items concurrently...")
            # Gather all tasks, including those that might be placeholders (None results)
            results = await asyncio.gather(*tasks, return_exceptions=True)

            print("Re-assembling data...")
            for i, item in enumerate(data):
                new_item = item.copy()  # Work on a copy
                original_path_result = results[i]  # Get the corresponding result

                if isinstance(item, dict) and "image_id" in item:
                    if isinstance(original_path_result, Exception):
                        print(
                            f"  Error fetching for image_id {item['image_id']}: {original_path_result}. Skipping URL addition."
                        )
                    elif (
                        original_path_result
                    ):  # Check if original_path_result is not None or empty
                        new_item["image_url"] = f"{url_prefix}{original_path_result}"
                        print(
                            f"  Processed item {i + 1}/{total_items}: Added image_url for image_id {item['image_id']}"
                        )
                    else:
                        # This handles cases where get_original_path returned None (e.g., path not found, or it was a placeholder)
                        print(
                            f"  Processed item {i + 1}/{total_items}: Failed to get or no original_path for image_id: {item['image_id']}. Skipping URL addition."
                        )
                else:
                    print(
                        f"  Skipping item {i + 1}/{total_items}: Not a dictionary or missing 'image_id'. Item: {item}"
                    )
                updated_data.append(new_item)

        print(f"Writing updated data to {output_path}...")
        with open(output_path, "w", encoding="utf-8") as outfile:
            json.dump(updated_data, outfile, indent=2, ensure_ascii=False)
        print("Processing complete.")

    except FileNotFoundError:
        print(f"Error: Input file not found at {input_path}")
    except MemoryError:
        print(
            f"MemoryError: The file {input_path} is too large to load into memory at once."
        )
        print("Consider if your JSON is in JSONL format (one JSON object per line).")
        print(
            "If so, you'll need to modify this script to read and process line by line."
        )

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {input_path}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during processing: {e}")


if __name__ == "__main__":
    input_json_file = "c:\\Github\\algo\\user_evaluations.json"
    output_json_file = "c:\\Github\\algo\\user_evaluations_with_urls.json"
    image_prefix = "https://imagebucket.nienie.xyz"

    asyncio.run(
        process_json_file(input_json_file, output_json_file, image_prefix)
    )  # Modified to use asyncio.run
