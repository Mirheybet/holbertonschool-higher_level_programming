#!/usr/bin/python3
import json
import requests
import csv


def fetch_and_print_posts():
    posts_url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(posts_url)
    print("Status Code:", response.status_code)

    if (response.status_code != 200):
        print("FAIL: def fetch_and_print_posts()")
    else:
        responses = response.json()
        for response in responses:
            print(response["title"])


def fetch_and_save_posts():
    posts_url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(posts_url)
    print("Status Code:", response.status_code)

    if (response.status_code == 200):
        responses = response.json()
        structured_posts = [{
            'id': response['id'],
            'title': response['title'],
            'body': response['body']
            } for response in responses]
        with open("post.csv", "w", newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(structured_posts)
            print("FILE:posts.csv created!")
    else:
        print("The CSV file was not created.")
