# wget -O /vantage6/vantage6-server/vantage6/server/controller/fixture.py https://raw.githubusercontent.com/jaspersnel/vantage6-server/collab-encryption-fix/vantage6/server/controller/fixture.py
vserver-local start -c /config.yaml &
sleep 5
vserver-local import -c /config.yaml /entities.yaml
tail -f /dev/null