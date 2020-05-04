{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-03-29T18:35:46.162138Z",
     "start_time": "2020-03-29T18:35:42.313283Z"
    }
   },
   "outputs": [],
   "source": [
    "from flask import Flask,render_template,request\n",
    "import boto3\n",
    "import glob\n",
    "import pandas as pd\n",
    "from datetime import date\n",
    "import numpy as np\n",
    "from matplotlib import pyplot as plt\n",
    "import cv2\n",
    "import os\n",
    "import openpyxl\n",
    "from apiclient.discovery import build\n",
    "from google_auth_oauthlib.flow import InstalledAppFlow\n",
    "import pickle\n",
    "from openpyxl.utils.dataframe import dataframe_to_rows\n",
    "from datetime import date\n",
    "import datetime\n",
    "from google.auth.transport.requests import Request"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-03-29T18:36:12.086040Z",
     "start_time": "2020-03-29T18:36:12.080038Z"
    }
   },
   "outputs": [],
   "source": [
    "app = Flask(__name__)\n",
    " \n",
    "yourAPIKEY = 'Attendance' "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-03-29T18:40:14.571680Z",
     "start_time": "2020-03-29T18:40:13.224515Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Restarting with stat\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Nikhil\\Anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py:3334: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "@app.route('/results/',methods=['POST']) \n",
    "def get_results():\n",
    "    keyword = request.form['Sname']  #getting input from user\n",
    "    \n",
    "    #print(keyword)\n",
    "    return render_template('frontpage.html',keyword)\n",
    " \n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
