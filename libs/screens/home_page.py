from kivymd.uix.screen import MDScreen


import json
#from libs.components.post_card import PostCard

#from libs.components.circular_avatar_image import CircularAvatarImage


class HomePage(MDScreen):
    profile_picture = 'http://127.0.0.1/fb.jpg'

    def on_enter(self):
        pass
        self.list_stories()
        self.list_posts()

    def list_stories(self):
        with open('assets/data/stories.json') as f_obj:
            data = json.load(f_obj)
            for name in data:
               pass
               self.ids.stories.add_widget(CircularAvatarImage(
                    avatar = data[name]['avatar'],
                    name = name
                ))
    
    def list_posts(self):
        with open('assets/data/posts.json') as f_obj:
            data = json.load(f_obj)
            for username in data:
                pass
                self.ids.timeline.add_widget(PostCard(
                    username = username,
                    avatar = data[username]['avatar'],
                    profile_pic = self.profile_picture,
                    post = data[username]['post'],
                    caption = data[username]['caption'],
                    likes = data[username]['likes'],
                    comments = data[username]['comments'],
                    posted_ago = data[username]['posted_ago'],
                ))