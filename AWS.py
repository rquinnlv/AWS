from boto.ec2.connection import EC2Connection
import boto, boto.ec2, sys

if __name__ == "__main__":
	conn = EC2Connection(sys.argv[3],sys.argv[4])
	regions = boto.ec2.regions(aws_access_key_id=sys.argv[3],aws_secret_access_key=sys.argv[4])
	west = regions[5]
	conn_west = west.connect(aws_access_key_id=sys.argv[3],aws_secret_access_key=sys.argv[4])
	o = int(sys.argv[1])
	t = int(sys.argv[2])
	
	conn_west.run_instances(sys.argv[5],o,t,instance_type='m1.medium')