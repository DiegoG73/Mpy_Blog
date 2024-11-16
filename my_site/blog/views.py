from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Diego",
        "date": date(2024, 11, 12),
        "title": "Nature At Its Best",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci assumenda tempora blanditiis rem, modi ab 
            odit provident id animi maxime fugiat, officiis eaque facere totam voluptatibus fugit consequuntur 
            temporibus unde?
            
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci assumenda tempora blanditiis rem, modi ab 
            odit provident id animi maxime fugiat, officiis eaque facere totam voluptatibus fugit consequuntur 
            temporibus unde?
            
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci assumenda tempora blanditiis rem, modi ab 
            odit provident id animi maxime fugiat, officiis eaque facere totam voluptatibus fugit consequuntur 
            temporibus unde?
            
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci assumenda tempora blanditiis rem, modi ab 
            odit provident id animi maxime fugiat, officiis eaque facere totam voluptatibus fugit consequuntur 
            temporibus unde?
        """
    },
    
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Diego",
        "date": date(2024, 11, 12),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci assumenda tempora blanditiis rem, modi ab 
            odit provident id animi maxime fugiat, officiis eaque facere totam voluptatibus fugit consequuntur 
            temporibus unde?
            
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci assumenda tempora blanditiis rem, modi ab 
            odit provident id animi maxime fugiat, officiis eaque facere totam voluptatibus fugit consequuntur 
            temporibus unde?
            
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci assumenda tempora blanditiis rem, modi ab 
            odit provident id animi maxime fugiat, officiis eaque facere totam voluptatibus fugit consequuntur 
            temporibus unde?
            
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci assumenda tempora blanditiis rem, modi ab 
            odit provident id animi maxime fugiat, officiis eaque facere totam voluptatibus fugit consequuntur 
            temporibus unde?
        """
    },
    
    {
        "slug": "coding",
        "image": "coding.jpg",
        "author": "Diego",
        "date": date(2024, 11, 12),
        "title": "Programming Is Great!",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci assumenda tempora blanditiis rem, modi ab 
            odit provident id animi maxime fugiat, officiis eaque facere totam voluptatibus fugit consequuntur 
            temporibus unde?
            
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci assumenda tempora blanditiis rem, modi ab 
            odit provident id animi maxime fugiat, officiis eaque facere totam voluptatibus fugit consequuntur 
            temporibus unde?
            
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci assumenda tempora blanditiis rem, modi ab 
            odit provident id animi maxime fugiat, officiis eaque facere totam voluptatibus fugit consequuntur 
            temporibus unde?
            
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci assumenda tempora blanditiis rem, modi ab 
            odit provident id animi maxime fugiat, officiis eaque facere totam voluptatibus fugit consequuntur 
            temporibus unde?
        """
    }
]

def get_date(post):
    return post['date']

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })