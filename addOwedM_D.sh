#!/bin/bash
      echo How much to add?
      read ADDNUMBER
	echo Comment?
	read COMMENT
      	echo "$ADDNUMBER - $COMMENT">>tabDetails.txt
python totalCalculator.py
