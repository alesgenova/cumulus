class ClusterType:
    EC2 = 'ec2'
    TRADITIONAL = 'trad'

    @staticmethod
    def is_valid_type(type):
        return type == ClusterType.EC2 or type == ClusterType.TRADITIONAL


class VolumeType:
    EBS = 'ebs'

    @staticmethod
    def is_valid_type(type):
        return type == VolumeType.EBS


class VolumeState:
    AVAILABLE = 'available'
    INUSE = 'in-use'
