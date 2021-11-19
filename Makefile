#!/usr/bin/make -f
##
## EPITECH PROJECT, 2021
## Groundhog
## File description:
## Makefile
##

NAME	=	groundhog
CC		=	cp
SRC		=	src/main.py

all:
	$(CC) $(SRC) $(NAME)
	chmod +x $(NAME)

clean:
	rm -f $(NAME)

fclean: clean

re: clean all