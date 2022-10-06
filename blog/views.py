from datetime import date

from django.shortcuts import render

POSTS = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountain.jpg",
        "author": "Ajay",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": """There's nothing like the views you get when hiking in the mountains!
          and I wasn;t even prepared for what happened whilst I was enjoying the
          view""",
        "content": """
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Et impedit numquam
    blanditiis quis in, voluptates, laborum tempore neque illo alias ipsam quasi
    rerum ex sint quae aliquid non voluptate vel!
    Lorem ipsum dolor, sit amet consectetur adipisicing elit. Et impedit numquam
    blanditiis quis in, voluptates, laborum tempore neque illo alias ipsam quasi
    rerum ex sint quae aliquid non voluptate vel!
        """,
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountain.jpg",
        "author": "Ajay",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking 2",
        "excerpt": """There's nothing like the views you get when hiking in the mountains!
          and I wasn;t even prepared for what happened whilst I was enjoying the
          view""",
        "content": """
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Et impedit numquam
    blanditiis quis in, voluptates, laborum tempore neque illo alias ipsam quasi
    rerum ex sint quae aliquid non voluptate vel!
    Lorem ipsum dolor, sit amet consectetur adipisicing elit. Et impedit numquam
    blanditiis quis in, voluptates, laborum tempore neque illo alias ipsam quasi
    rerum ex sint quae aliquid non voluptate vel!
        """,
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountain.jpg",
        "author": "Ajay",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking 3",
        "excerpt": """There's nothing like the views you get when hiking in the mountains!
          and I wasn;t even prepared for what happened whilst I was enjoying the
          view""",
        "content": """
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Et impedit numquam
    blanditiis quis in, voluptates, laborum tempore neque illo alias ipsam quasi
    rerum ex sint quae aliquid non voluptate vel!
    Lorem ipsum dolor, sit amet consectetur adipisicing elit. Et impedit numquam
    blanditiis quis in, voluptates, laborum tempore neque illo alias ipsam quasi
    rerum ex sint quae aliquid non voluptate vel!
        """,
    },
]


def get_date(post):
    return post.get("date")


# Create your views here.
def starting_page(request):
    sorted_posts = sorted(POSTS, key=get_date)
    latest_post = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_post})


def posts(request):
    return render(request, "blog/all-posts.html", {"all_posts": POSTS})


def post_detail(request, slug):
    identified_post = next(post for post in POSTS if post.get("slug") == slug)
    return render(request, "blog/post-detail.html", {"post": identified_post})
