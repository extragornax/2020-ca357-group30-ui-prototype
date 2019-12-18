# 2020-ca357-group30-ui-prototype

# Synopsis DCU Dashboard
Simple django based project to help the DCU students and staff have quicker access to their timetable, announcements, books loans and more, on a single ergonomic page.

# Run and install
The production version of this project is hosted on [here](http://vps.cheap.appboxes.co:10127/) but you can also run it locally

## Local install
The project is hosted on Gitlab, git will be used to pull it.
> **SSH**: git clone git@gitlab.computing.dcu.ie:trama2/2020-ca357-group30-ui-prototype.git

> **HTTP**: git clone https://gitlab.computing.dcu.ie/trama2/2020-ca357-group30-ui-prototype.git

Then **cd** in the folder **22020-ca357-group30-ui-prototype**

**Python3.6** and **pip3** are required
Depending on your system, you can install them like that:
> sudo apt-get install python3 python3-pip

We will then install the dependencies for the project

> pip3 install -r requirements.txt


Once everything is correctly installed, we will now setup the database. Access the src folder
> cd frontend-django

Now let's migrate the database with
> python3 manage.py migrate

Once all of this is done
you can run 
> python3 manage.py runserver

The website is now accessible on
> http://localhost:8000

## Contributors
Gaspard WITRAND
\<gaspard.witrand2@mail.dcu.ie\> 
[Gitlab DCU](https://gitlab.computing.dcu.ie/witrang2) - [Github](https://github.com/extragornax) - [Gitlab](https://gitlab.com/extragornax)

Anthony TRAM \<anthony.tram2@mail.dcu.ie\> [Gitlab DCU](https://gitlab.computing.dcu.ie/trama2) - [Github](https://github.com/dotcheap)

Arthur PHILIPPE \<arthur.philippe4@mail.dcu.ie\> [Gitlab DCU](https://gitlab.computing.dcu.ie/philipa4) - [Github](https://github.com/arthurphilippe)

Florence HU \<florence.hu6@mail.dcu.ie\> [Gitlab DCU](https://gitlab.computing.dcu.ie/huf6)

## License
[MIT License](https://opensource.org/licenses/MIT)

Copyright (c) 2019 Gaspard WITRAND - Anthony TRAM - Arthur PHILIPPE - Florence HU

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.