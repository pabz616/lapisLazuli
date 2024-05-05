"""
Common injection parameters
src: https://swisskyrepo.github.io/PayloadsAllTheThings/Open%20Redirect/#filter-bypass
"""

import random


class InjectionParameters:
    def select_injection_parameters():
        params = [
            '?next=', '?url=', '?target=', '?rurl=', '?dest=', '?destination=', '?redir=', '?redirect_uri=',
            '?redirect_url=', '?redirect=', '/redirect/', '/cgi-bin/redirect.cgi?', '/out/', '/out?', '?view=',
            '/login?to=', '?image_url=', '?go=', '?return=', '?returnTo=', '?return_to=', '?checkout_url=', '?continue=',
            '?return_path=']
        
        injection_parameters = random.choice(params)
        return injection_parameters