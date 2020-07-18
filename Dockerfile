FROM python
WORKDIR /mnt
ADD ./ ./
CMD ["/bin/sh"]