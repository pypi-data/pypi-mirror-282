# terminaloptions

Menu for command line applications.

## Installation

```bash
pip install terminaloptions
```

## Usage

```python
from terminaloptions import Menu

options = [
    'Option 1',
    'Option 2',
    'Option 3',
]

menu = Menu(options) # Create a new menu.

# Running menu will print the options and wait for the user to select one.
# Use the arrow keys to navigate and enter to select.

selection = menu.run_menu() # Returns the selected option.
```

Other arguments for `run_menu` method:

- `title`: str | None = None -> Show a title for the menu.
- `get_index`: bool = False -> Return the index of the selected option.
- `help`: bool = True -> Show a short help message at the top of the menu.

## Next features

- <span style="font-family: 'courier new'">[ ]</span> Add support for submenus.
- <span style="font-family: 'courier new'">[ ]</span> Customise the appearance of the menu.
- <span style="font-family: 'courier new'">[ ]</span> Add support for custom key bindings.
- <span style="font-family: 'courier new'">[ ]</span> Add support for custom actions.
- <span style="font-family: 'courier new'">[ ]</span> Add support for custom help messages.