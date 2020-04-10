#!/bin/bash
      echo How much to add?
      read ADDNUMBER
	echo Comment?
	read COMMENT
      	echo "$ADDNUMBER - $COMMENT">>moneyIOweM_D.txt
python total.py
source ../.~bash_aliases
gupdate
