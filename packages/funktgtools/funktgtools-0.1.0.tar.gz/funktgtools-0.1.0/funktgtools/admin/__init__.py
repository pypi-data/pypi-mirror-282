from .admin_funcs import admin_router # Includes .forwarding by default
#from .forwarding import (forward_router)

from markup import (
    mass_button_markup, 
    gen_link_markup, 
    create_yes_no_markup, 
    dynamic_dictionary_markup, 
    add_navigation_button_markup
)
from .config import BotConfig


from locker import LOCKER, Locker