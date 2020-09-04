# Lambdata

Lambdata is a test package created for educational purpoises and functionality test

## Installation

To install, copy:

`pip install -i https://test.pypi.org/simple/ lambdata-kilovolt`



## Usage

```Firearms
from lambdata.oop_examples import Firearms

Firearms('name', 'caliber', 'country', 'selector position, default=0')
Firearms.selector_safety() # changes selector position to 0, returns 'Safety is on'
Firearms.selector_fire() # changes selector position to 1, returns 'Semi'


Rifles - inherited sublass from firearms, has selector postition 2. 
Rifles.full_auto() #puts selector on 2, returns 'full auto'. 
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)