# define csd3:cclake parameters common across reframe partitions:
csd3_cclake_common = {
    'scheduler': 'slurm',
    'launcher': 'srun',
    'access': [
        '--partition=cclake',
        '--account=support-cpu',
        '--exclude=cpu-p-[1-280,337-672]', # only use one rack's-worth of nodes at present: use rack 6 (cpu-p-[281-336]) as this is all ok
        ],
    'max_jobs': 20,
}

# define um6p parameters common across reframe partitions:
um6p_common = {
    'scheduler': 'slurm',
    'launcher': 'srun',
    'access': [
        # use rack h21a8 only:
        '--exclude=cpu-h21a5-u1-svn2,cpu-h21a5-u1-svn4,cpu-h21a5-u2-svn1,cpu-h21a5-u2-svn3,cpu-h21a5-u3-svn2,cpu-h21a5-u3-svn4,cpu-h21a5-u4-svn1,cpu-h21a5-u4-svn3,cpu-h21a5-u5-svn2,cpu-h21a5-u5-svn4,cpu-h21a5-u6-svn1,cpu-h21a5-u6-svn3,cpu-h21a5-u7-svn2,cpu-h21a5-u7-svn4,cpu-h21a5-u8-svn1,cpu-h21a5-u8-svn3,cpu-h21a5-u9-svn2,cpu-h21a5-u9-svn4,cpu-h21a5-u10-svn1,cpu-h21a5-u10-svn3,cpu-h21a5-u11-svn2,cpu-h21a5-u11-svn4,cpu-h21a5-u12-svn1,cpu-h21a5-u12-svn3,cpu-h21a5-u13-svn2,cpu-h21a5-u13-svn4,cpu-h21a5-u14-svn1,cpu-h21a5-u14-svn3,cpu-h21a5-u23-svn2,cpu-h21a5-u23-svn4,cpu-h21a5-u24-svn1,cpu-h21a5-u24-svn3,cpu-h21a5-u25-svn2,cpu-h21a5-u25-svn4,cpu-h21a5-u26-svn1,cpu-h21a5-u26-svn3,cpu-h21a5-u27-svn2,cpu-h21a5-u27-svn4,cpu-h21a5-u28-svn1,cpu-h21a5-u28-svn3,cpu-h21a5-u29-svn2,cpu-h21a5-u29-svn4,cpu-h21a5-u30-svn1,cpu-h21a5-u30-svn3,cpu-h21a5-u31-svn2,cpu-h21a5-u31-svn4,cpu-h21a5-u32-svn1,cpu-h21a5-u32-svn3,cpu-h21a5-u33-svn2,cpu-h21a5-u33-svn4,cpu-h21a5-u34-svn1,cpu-h21a5-u34-svn3,cpu-h21a5-u35-svn2,cpu-h21a5-u35-svn4,cpu-h21a5-u36-svn1,cpu-h21a5-u36-svn3,cpu-h21b5-u1-svn2,cpu-h21b5-u1-svn4,cpu-h21b5-u2-svn1,cpu-h21b5-u2-svn3,cpu-h21b5-u3-svn2,cpu-h21b5-u3-svn4,cpu-h21b5-u4-svn1,cpu-h21b5-u4-svn3,cpu-h21b5-u5-svn2,cpu-h21b5-u5-svn4,cpu-h21b5-u6-svn1,cpu-h21b5-u6-svn3,cpu-h21b5-u7-svn2,cpu-h21b5-u7-svn4,cpu-h21b5-u8-svn1,cpu-h21b5-u8-svn3,cpu-h21b5-u9-svn2,cpu-h21b5-u9-svn4,cpu-h21b5-u10-svn1,cpu-h21b5-u10-svn3,cpu-h21b5-u11-svn2,cpu-h21b5-u11-svn4,cpu-h21b5-u12-svn1,cpu-h21b5-u12-svn3,cpu-h21b5-u13-svn2,cpu-h21b5-u13-svn4,cpu-h21b5-u14-svn1,cpu-h21b5-u14-svn3,cpu-h21b5-u23-svn2,cpu-h21b5-u23-svn4,cpu-h21b5-u24-svn1,cpu-h21b5-u24-svn3,cpu-h21b5-u25-svn2,cpu-h21b5-u25-svn4,cpu-h21b5-u26-svn1,cpu-h21b5-u26-svn3,cpu-h21b5-u27-svn2,cpu-h21b5-u27-svn4,cpu-h21b5-u28-svn1,cpu-h21b5-u28-svn3,cpu-h21b5-u29-svn2,cpu-h21b5-u29-svn4,cpu-h21b5-u30-svn1,cpu-h21b5-u30-svn3,cpu-h21b5-u31-svn2,cpu-h21b5-u31-svn4,cpu-h21b5-u32-svn1,cpu-h21b5-u32-svn3,cpu-h21b5-u33-svn2,cpu-h21b5-u33-svn4,cpu-h21b5-u34-svn1,cpu-h21b5-u34-svn3,cpu-h21b5-u35-svn2,cpu-h21b5-u35-svn4,cpu-h21b5-u36-svn1,cpu-h21b5-u36-svn3,cpu-h21c5-u1-svn2,cpu-h21c5-u1-svn4,cpu-h21c5-u2-svn1,cpu-h21c5-u2-svn3,cpu-h21c5-u3-svn2,cpu-h21c5-u3-svn4,cpu-h21c5-u4-svn1,cpu-h21c5-u4-svn3,cpu-h21c5-u5-svn2,cpu-h21c5-u5-svn4,cpu-h21c5-u6-svn1,cpu-h21c5-u6-svn3,cpu-h21c5-u7-svn2,cpu-h21c5-u7-svn4,cpu-h21c5-u8-svn1,cpu-h21c5-u8-svn3,cpu-h21c5-u9-svn2,cpu-h21c5-u9-svn4,cpu-h21c5-u10-svn1,cpu-h21c5-u10-svn3,cpu-h21c5-u11-svn2,cpu-h21c5-u11-svn4,cpu-h21c5-u12-svn1,cpu-h21c5-u12-svn3,cpu-h21c5-u13-svn2,cpu-h21c5-u13-svn4,cpu-h21c5-u14-svn1,cpu-h21c5-u14-svn3,cpu-h21c5-u23-svn2,cpu-h21c5-u23-svn4,cpu-h21c5-u24-svn1,cpu-h21c5-u24-svn3,cpu-h21c5-u25-svn2,cpu-h21c5-u25-svn4,cpu-h21c5-u26-svn1,cpu-h21c5-u26-svn3,cpu-h21c5-u27-svn2,cpu-h21c5-u27-svn4,cpu-h21c5-u28-svn1,cpu-h21c5-u28-svn3,cpu-h21c5-u29-svn2,cpu-h21c5-u29-svn4,cpu-h21c5-u30-svn1,cpu-h21c5-u30-svn3,cpu-h21c5-u31-svn2,cpu-h21c5-u31-svn4,cpu-h21c5-u32-svn1,cpu-h21c5-u32-svn3,cpu-h21c5-u33-svn2,cpu-h21c5-u33-svn4,cpu-h21c5-u34-svn1,cpu-h21c5-u34-svn3,cpu-h21c5-u35-svn2,cpu-h21c5-u35-svn4,cpu-h21c5-u36-svn1,cpu-h21c5-u36-svn3,cpu-h21c8-u1-svn2,cpu-h21c8-u1-svn4,cpu-h21c8-u2-svn1,cpu-h21c8-u2-svn3,cpu-h21c8-u3-svn2,cpu-h21c8-u3-svn4,cpu-h21c8-u4-svn1,cpu-h21c8-u4-svn3,cpu-h21c8-u5-svn2,cpu-h21c8-u5-svn4,cpu-h21c8-u6-svn1,cpu-h21c8-u6-svn3,cpu-h21c8-u7-svn2,cpu-h21c8-u7-svn4,cpu-h21c8-u8-svn1,cpu-h21c8-u8-svn3,cpu-h21c8-u9-svn2,cpu-h21c8-u9-svn4,cpu-h21c8-u10-svn1,cpu-h21c8-u10-svn3,cpu-h21c8-u11-svn2,cpu-h21c8-u11-svn4,cpu-h21c8-u12-svn1,cpu-h21c8-u12-svn3,cpu-h21c8-u13-svn2,cpu-h21c8-u13-svn4,cpu-h21c8-u14-svn1,cpu-h21c8-u14-svn3,cpu-h21c8-u23-svn2,cpu-h21c8-u23-svn4,cpu-h21c8-u24-svn1,cpu-h21c8-u24-svn3,cpu-h21c8-u25-svn2,cpu-h21c8-u25-svn4,cpu-h21c8-u26-svn1,cpu-h21c8-u26-svn3,cpu-h21c8-u27-svn2,cpu-h21c8-u27-svn4,cpu-h21c8-u28-svn1,cpu-h21c8-u28-svn3,cpu-h21c8-u29-svn2,cpu-h21c8-u29-svn4,cpu-h21c8-u30-svn1,cpu-h21c8-u30-svn3,cpu-h21c8-u31-svn2,cpu-h21c8-u31-svn4,cpu-h21c8-u32-svn1,cpu-h21c8-u32-svn3,cpu-h21c8-u33-svn2,cpu-h21c8-u33-svn4,cpu-h21c8-u34-svn1,cpu-h21c8-u34-svn3,cpu-h21c8-u35-svn2,cpu-h21c8-u35-svn4,cpu-h21c8-u36-svn1,cpu-h21c8-u36-svn3,cpu-h21d5-u1-svn2,cpu-h21d5-u1-svn4,cpu-h21d5-u2-svn1,cpu-h21d5-u2-svn3,cpu-h21d5-u3-svn2,cpu-h21d5-u3-svn4,cpu-h21d5-u4-svn1,cpu-h21d5-u4-svn3,cpu-h21d5-u5-svn2,cpu-h21d5-u5-svn4,cpu-h21d5-u6-svn1,cpu-h21d5-u6-svn3,cpu-h21d5-u7-svn2,cpu-h21d5-u7-svn4,cpu-h21d5-u8-svn1,cpu-h21d5-u8-svn3,cpu-h21d5-u9-svn2,cpu-h21d5-u9-svn4,cpu-h21d5-u10-svn1,cpu-h21d5-u10-svn3,cpu-h21d5-u11-svn2,cpu-h21d5-u11-svn4,cpu-h21d5-u12-svn1,cpu-h21d5-u12-svn3,cpu-h21d5-u13-svn2,cpu-h21d5-u13-svn4,cpu-h21d5-u14-svn1,cpu-h21d5-u14-svn3,cpu-h21d5-u23-svn2,cpu-h21d5-u23-svn4,cpu-h21d5-u24-svn1,cpu-h21d5-u24-svn3,cpu-h21d5-u25-svn2,cpu-h21d5-u25-svn4,cpu-h21d5-u26-svn1,cpu-h21d5-u26-svn3,cpu-h21d5-u27-svn2,cpu-h21d5-u27-svn4,cpu-h21d5-u28-svn1,cpu-h21d5-u28-svn3,cpu-h21d5-u29-svn2,cpu-h21d5-u29-svn4,cpu-h21d5-u30-svn1,cpu-h21d5-u30-svn3,cpu-h21d5-u31-svn2,cpu-h21d5-u31-svn4,cpu-h21d5-u32-svn1,cpu-h21d5-u32-svn3,cpu-h21d5-u33-svn2,cpu-h21d5-u33-svn4,cpu-h21d5-u34-svn1,cpu-h21d5-u34-svn3,cpu-h21d5-u35-svn2,cpu-h21d5-u35-svn4,cpu-h21d5-u36-svn1,cpu-h21d5-u36-svn3,cpu-h22a5-u26-sv,cpu-h22a5-u27-sv,cpu-h22a5-u28-sv,cpu-h22a5-u29-sv,cpu-h22a5-u34-sv,cpu-h22a5-u35-sv,cpu-h22a5-u37-sv,cpu-h22a5-u39-sv,cpu-h22a5-u41-sv,cpu-h22a8-u1-sv,cpu-h22a8-u3-sv,cpu-h22a8-u5-sv,cpu-h22a8-u7-sv,cpu-h22a8-u9-sv,cpu-h22a8-u11-svn2,cpu-h22a8-u11-svn4,cpu-h22a8-u12-svn1,cpu-h22a8-u12-svn3,cpu-h22a8-u13-svn2,cpu-h22a8-u13-svn4,cpu-h22a8-u14-svn1,cpu-h22a8-u14-svn3,cpu-h22a8-u15-svn2,cpu-h22a8-u15-svn4,cpu-h22a8-u16-svn1,cpu-h22a8-u16-svn3,cpu-h22a8-u17-sv,cpu-h22a8-u18-sv,cpu-h22a8-u20-sv,cpu-h22a8-u26-sv,cpu-h22a8-u28-sv,cpu-h22a8-u30-sv,cpu-h22b5-u1-svn2,cpu-h22b5-u1-svn4,cpu-h22b5-u2-svn1,cpu-h22b5-u2-svn3,cpu-h22b5-u3-svn2,cpu-h22b5-u3-svn4,cpu-h22b5-u4-svn1,cpu-h22b5-u4-svn3,cpu-h22b5-u5-svn2,cpu-h22b5-u5-svn4,cpu-h22b5-u6-svn1,cpu-h22b5-u6-svn3,cpu-h22b5-u7-svn2,cpu-h22b5-u7-svn4,cpu-h22b5-u8-svn1,cpu-h22b5-u8-svn3,cpu-h22b5-u9-svn2,cpu-h22b5-u9-svn4,cpu-h22b5-u10-svn1,cpu-h22b5-u10-svn3,cpu-h22b5-u11-svn2,cpu-h22b5-u11-svn4,cpu-h22b5-u12-svn1,cpu-h22b5-u12-svn3,cpu-h22b5-u13-svn2,cpu-h22b5-u13-svn4,cpu-h22b5-u14-svn1,cpu-h22b5-u14-svn3,cpu-h22b5-u23-svn2,cpu-h22b5-u23-svn4,cpu-h22b5-u24-svn1,cpu-h22b5-u24-svn3,cpu-h22b5-u25-svn2,cpu-h22b5-u25-svn4,cpu-h22b5-u26-svn1,cpu-h22b5-u26-svn3,cpu-h22b5-u27-svn2,cpu-h22b5-u27-svn4,cpu-h22b5-u28-svn1,cpu-h22b5-u28-svn3,cpu-h22b5-u29-svn2,cpu-h22b5-u29-svn4,cpu-h22b5-u30-svn1,cpu-h22b5-u30-svn3,cpu-h22b5-u31-svn2,cpu-h22b5-u31-svn4,cpu-h22b5-u32-svn1,cpu-h22b5-u32-svn3,cpu-h22b5-u33-svn2,cpu-h22b5-u33-svn4,cpu-h22b5-u34-svn1,cpu-h22b5-u34-svn3,cpu-h22b5-u35-svn2,cpu-h22b5-u35-svn4,cpu-h22b5-u36-svn1,cpu-h22b5-u36-svn3,cpu-h22b8-u1-svn2,cpu-h22b8-u1-svn4,cpu-h22b8-u2-svn1,cpu-h22b8-u2-svn3,cpu-h22b8-u3-svn2,cpu-h22b8-u3-svn4,cpu-h22b8-u4-svn1,cpu-h22b8-u4-svn3,cpu-h22b8-u5-svn2,cpu-h22b8-u5-svn4,cpu-h22b8-u6-svn1,cpu-h22b8-u6-svn3,cpu-h22b8-u7-svn2,cpu-h22b8-u7-svn4,cpu-h22b8-u8-svn1,cpu-h22b8-u8-svn3,cpu-h22b8-u9-svn2,cpu-h22b8-u9-svn4,cpu-h22b8-u10-svn1,cpu-h22b8-u10-svn3,cpu-h22b8-u11-svn2,cpu-h22b8-u11-svn4,cpu-h22b8-u12-svn1,cpu-h22b8-u12-svn3,cpu-h22b8-u13-svn2,cpu-h22b8-u13-svn4,cpu-h22b8-u14-svn1,cpu-h22b8-u14-svn3,cpu-h22b8-u23-svn2,cpu-h22b8-u23-svn4,cpu-h22b8-u24-svn1,cpu-h22b8-u24-svn3,cpu-h22b8-u25-svn2,cpu-h22b8-u25-svn4,cpu-h22b8-u26-svn1,cpu-h22b8-u26-svn3,cpu-h22b8-u27-svn2,cpu-h22b8-u27-svn4,cpu-h22b8-u28-svn1,cpu-h22b8-u28-svn3,cpu-h22b8-u29-svn2,cpu-h22b8-u29-svn4,cpu-h22b8-u30-svn1,cpu-h22b8-u30-svn3,cpu-h22b8-u31-svn2,cpu-h22b8-u31-svn4,cpu-h22b8-u32-svn1,cpu-h22b8-u32-svn3,cpu-h22b8-u33-svn2,cpu-h22b8-u33-svn4,cpu-h22b8-u34-svn1,cpu-h22b8-u34-svn3,cpu-h22b8-u35-svn2,cpu-h22b8-u35-svn4,cpu-h22b8-u36-svn1,cpu-h22b8-u36-svn3,cpu-h22c5-u1-svn2,cpu-h22c5-u1-svn4,cpu-h22c5-u2-svn1,cpu-h22c5-u2-svn3,cpu-h22c5-u3-svn2,cpu-h22c5-u3-svn4,cpu-h22c5-u4-svn1,cpu-h22c5-u4-svn3,cpu-h22c5-u5-svn2,cpu-h22c5-u5-svn4,cpu-h22c5-u6-svn1,cpu-h22c5-u6-svn3,cpu-h22c5-u7-svn2,cpu-h22c5-u7-svn4,cpu-h22c5-u8-svn1,cpu-h22c5-u8-svn3,cpu-h22c5-u9-svn2,cpu-h22c5-u9-svn4,cpu-h22c5-u10-svn1,cpu-h22c5-u10-svn3,cpu-h22c5-u11-svn2,cpu-h22c5-u11-svn4,cpu-h22c5-u12-svn1,cpu-h22c5-u12-svn3,cpu-h22c5-u13-svn2,cpu-h22c5-u13-svn4,cpu-h22c5-u14-svn1,cpu-h22c5-u14-svn3,cpu-h22c5-u23-svn2,cpu-h22c5-u23-svn4,cpu-h22c5-u24-svn1,cpu-h22c5-u24-svn3,cpu-h22c5-u25-svn2,cpu-h22c5-u25-svn4,cpu-h22c5-u26-svn1,cpu-h22c5-u26-svn3,cpu-h22c5-u27-svn2,cpu-h22c5-u27-svn4,cpu-h22c5-u28-svn1,cpu-h22c5-u28-svn3,cpu-h22c5-u29-svn2,cpu-h22c5-u29-svn4,cpu-h22c5-u30-svn1,cpu-h22c5-u30-svn3,cpu-h22c5-u31-svn2,cpu-h22c5-u31-svn4,cpu-h22c5-u32-svn1,cpu-h22c5-u32-svn3,cpu-h22c5-u33-svn2,cpu-h22c5-u33-svn4,cpu-h22c5-u34-svn1,cpu-h22c5-u34-svn3,cpu-h22c5-u35-svn2,cpu-h22c5-u35-svn4,cpu-h22c5-u36-svn1,cpu-h22c5-u36-svn3,cpu-h22d5-u1-svn2,cpu-h22d5-u1-svn4,cpu-h22d5-u2-svn1,cpu-h22d5-u2-svn3,cpu-h22d5-u3-svn2,cpu-h22d5-u3-svn4,cpu-h22d5-u4-svn1,cpu-h22d5-u4-svn3,cpu-h22d5-u5-svn2,cpu-h22d5-u5-svn4,cpu-h22d5-u6-svn1,cpu-h22d5-u6-svn3,cpu-h22d5-u7-svn2,cpu-h22d5-u7-svn4,cpu-h22d5-u8-svn1,cpu-h22d5-u8-svn3,cpu-h22d5-u9-svn2,cpu-h22d5-u9-svn4,cpu-h22d5-u10-svn1,cpu-h22d5-u10-svn3,cpu-h22d5-u11-svn2,cpu-h22d5-u11-svn4,cpu-h22d5-u12-svn1,cpu-h22d5-u12-svn3,cpu-h22d5-u13-svn2,cpu-h22d5-u13-svn4,cpu-h22d5-u14-svn1,cpu-h22d5-u14-svn3,cpu-h22d5-u23-svn2,cpu-h22d5-u23-svn4,cpu-h22d5-u24-svn1,cpu-h22d5-u24-svn3,cpu-h22d5-u25-svn2,cpu-h22d5-u25-svn4,cpu-h22d5-u26-svn1,cpu-h22d5-u26-svn3,cpu-h22d5-u27-svn2,cpu-h22d5-u27-svn4,cpu-h22d5-u28-svn1,cpu-h22d5-u28-svn3,cpu-h22d5-u29-svn2,cpu-h22d5-u29-svn4,cpu-h22d5-u30-svn1,cpu-h22d5-u30-svn3,cpu-h22d5-u31-svn2,cpu-h22d5-u31-svn4,cpu-h22d5-u32-svn1,cpu-h22d5-u32-svn3,cpu-h22d5-u33-svn2,cpu-h22d5-u33-svn4,cpu-h22d5-u34-svn1,cpu-h22d5-u34-svn3,cpu-h22d5-u35-svn2,'
        'cpu-h22d5-u35-svn4,cpu-h22d5-u36-svn1,cpu-h22d5-u36-svn3,cpu-h22d5-u37-sv,cpu-h22d8-u1-svn2,cpu-h22d8-u1-svn4,cpu-h22d8-u2-svn1,cpu-h22d8-u2-svn3,cpu-h22d8-u3-svn2,cpu-h22d8-u3-svn4,cpu-h22d8-u4-svn1,cpu-h22d8-u4-svn3,cpu-h22d8-u5-svn2,cpu-h22d8-u5-svn4,cpu-h22d8-u6-svn1,cpu-h22d8-u6-svn3,cpu-h22d8-u7-svn2,cpu-h22d8-u7-svn4,cpu-h22d8-u8-svn1,cpu-h22d8-u8-svn3,cpu-h22d8-u9-svn2,cpu-h22d8-u9-svn4,cpu-h22d8-u10-svn1,cpu-h22d8-u10-svn3,cpu-h22d8-u11-svn2,cpu-h22d8-u11-svn4,cpu-h22d8-u12-svn1,cpu-h22d8-u12-svn3,cpu-h22d8-u13-svn2,cpu-h22d8-u13-svn4,cpu-h22d8-u14-svn1,cpu-h22d8-u14-svn3,cpu-h22d8-u23-svn2,cpu-h22d8-u23-svn4,cpu-h22d8-u24-svn1,cpu-h22d8-u24-svn3,cpu-h22d8-u25-svn2,cpu-h22d8-u25-svn4,cpu-h22d8-u26-svn1,cpu-h22d8-u26-svn3,cpu-h22d8-u27-svn2,cpu-h22d8-u27-svn4,cpu-h22d8-u28-svn1,cpu-h22d8-u28-svn3,cpu-h22d8-u29-svn2,cpu-h22d8-u29-svn4,cpu-h22d8-u30-svn1,cpu-h22d8-u30-svn3,cpu-h22d8-u31-svn2,cpu-h22d8-u31-svn4,cpu-h22d8-u32-svn1,cpu-h22d8-u32-svn3,cpu-h22d8-u33-svn2,cpu-h22d8-u33-svn4,cpu-h22d8-u34-svn1,cpu-h22d8-u34-svn3,cpu-h22d8-u35-svn2,cpu-h22d8-u35-svn4,cpu-h22d8-u36-svn1,cpu-h22d8-u36-svn3,cpu-h22d8-u37-sv,cpu-h23a5-u1-svn2,cpu-h23a5-u1-svn4,cpu-h23a5-u2-svn1,cpu-h23a5-u2-svn3,cpu-h23a5-u3-svn2,cpu-h23a5-u3-svn4,cpu-h23a5-u4-svn1,cpu-h23a5-u4-svn3,cpu-h23a5-u5-svn2,cpu-h23a5-u5-svn4,cpu-h23a5-u6-svn1,cpu-h23a5-u6-svn3,cpu-h23a5-u7-svn2,cpu-h23a5-u7-svn4,cpu-h23a5-u8-svn1,cpu-h23a5-u8-svn3,cpu-h23a5-u9-svn2,cpu-h23a5-u9-svn4,cpu-h23a5-u10-svn1,cpu-h23a5-u10-svn3,cpu-h23a5-u11-svn2,cpu-h23a5-u11-svn4,cpu-h23a5-u12-svn1,cpu-h23a5-u12-svn3,cpu-h23a5-u13-svn2,cpu-h23a5-u13-svn4,cpu-h23a5-u14-svn1,cpu-h23a5-u14-svn3,cpu-h23a5-u23-svn2,cpu-h23a5-u23-svn4,cpu-h23a5-u24-svn1,cpu-h23a5-u24-svn3,cpu-h23a5-u25-svn2,cpu-h23a5-u25-svn4,cpu-h23a5-u26-svn3,cpu-h23a5-u27-svn2,cpu-h23a5-u27-svn4,cpu-h23a5-u28-svn1,cpu-h23a5-u28-svn3,cpu-h23a5-u29-svn2,cpu-h23a5-u29-svn4,cpu-h23a5-u30-svn1,cpu-h23a5-u30-svn3,cpu-h23a5-u31-svn2,cpu-h23a5-u31-svn4,cpu-h23a5-u32-svn1,cpu-h23a5-u32-svn3,cpu-h23a5-u33-svn2,cpu-h23a5-u33-svn4,cpu-h23a5-u34-svn1,cpu-h23a5-u34-svn3,cpu-h23a5-u35-svn2,cpu-h23a5-u35-svn4,cpu-h23a5-u36-svn1,cpu-h23a5-u36-svn3,cpu-h23a8-u1-svn2,cpu-h23a8-u1-svn4,cpu-h23a8-u2-svn1,cpu-h23a8-u2-svn3,cpu-h23a8-u3-svn2,cpu-h23a8-u3-svn4,cpu-h23a8-u4-svn1,cpu-h23a8-u4-svn3,cpu-h23a8-u5-svn2,cpu-h23a8-u5-svn4,cpu-h23a8-u6-svn1,cpu-h23a8-u6-svn3,cpu-h23a8-u7-svn2,cpu-h23a8-u7-svn4,cpu-h23a8-u8-svn1,cpu-h23a8-u8-svn3,cpu-h23a8-u9-svn2,cpu-h23a8-u9-svn4,cpu-h23a8-u10-svn1,cpu-h23a8-u10-svn3,cpu-h23a8-u11-svn2,cpu-h23a8-u11-svn4,cpu-h23a8-u12-svn1,cpu-h23a8-u12-svn3,cpu-h23a8-u13-svn2,cpu-h23a8-u13-svn4,cpu-h23a8-u14-svn1,cpu-h23a8-u14-svn3,cpu-h23a8-u23-svn2,cpu-h23a8-u24-svn1,cpu-h23a8-u24-svn3,cpu-h23a8-u25-svn2,cpu-h23a8-u25-svn4,cpu-h23a8-u26-svn1,cpu-h23a8-u26-svn3,cpu-h23a8-u27-svn2,cpu-h23a8-u27-svn4,cpu-h23a8-u28-svn1,cpu-h23a8-u28-svn3,cpu-h23a8-u29-svn2,cpu-h23a8-u29-svn4,cpu-h23a8-u30-svn1,cpu-h23a8-u30-svn3,cpu-h23a8-u31-svn2,cpu-h23a8-u31-svn4,cpu-h23a8-u32-svn1,cpu-h23a8-u32-svn3,cpu-h23a8-u33-svn2,cpu-h23a8-u33-svn4,cpu-h23a8-u34-svn1,cpu-h23a8-u34-svn3,cpu-h23a8-u35-svn2,cpu-h23a8-u35-svn4,cpu-h23a8-u36-svn1,cpu-h23a8-u36-svn3,cpu-h23b5-u1-svn2,cpu-h23b5-u1-svn4,cpu-h23b5-u2-svn1,cpu-h23b5-u2-svn3,cpu-h23b5-u3-svn2,cpu-h23b5-u3-svn4,cpu-h23b5-u4-svn1,cpu-h23b5-u4-svn3,cpu-h23b5-u5-svn2,cpu-h23b5-u5-svn4,cpu-h23b5-u6-svn1,cpu-h23b5-u6-svn3,cpu-h23b5-u7-svn2,cpu-h23b5-u7-svn4,cpu-h23b5-u8-svn1,cpu-h23b5-u8-svn3,cpu-h23b5-u9-svn2,cpu-h23b5-u9-svn4,cpu-h23b5-u10-svn1,cpu-h23b5-u10-svn3,cpu-h23b5-u11-svn2,cpu-h23b5-u11-svn4,cpu-h23b5-u12-svn1,cpu-h23b5-u12-svn3,cpu-h23b5-u13-svn2,cpu-h23b5-u13-svn4,cpu-h23b5-u14-svn1,cpu-h23b5-u14-svn3,cpu-h23b5-u23-svn2,cpu-h23b5-u23-svn4,cpu-h23b5-u24-svn1,cpu-h23b5-u24-svn3,cpu-h23b5-u25-svn2,cpu-h23b5-u25-svn4,cpu-h23b5-u26-svn1,cpu-h23b5-u26-svn3,cpu-h23b5-u27-svn2,cpu-h23b5-u27-svn4,cpu-h23b5-u28-svn1,cpu-h23b5-u28-svn3,cpu-h23b5-u29-svn2,cpu-h23b5-u29-svn4,cpu-h23b5-u30-svn1,cpu-h23b5-u30-svn3,cpu-h23b5-u31-svn2,cpu-h23b5-u31-svn4,cpu-h23b5-u32-svn1,cpu-h23b5-u32-svn3,cpu-h23b5-u33-svn2,cpu-h23b5-u33-svn4,cpu-h23b5-u34-svn1,cpu-h23b5-u34-svn3,cpu-h23b5-u35-svn2,cpu-h23b5-u35-svn4,cpu-h23b5-u36-svn1,cpu-h23b5-u36-svn3,cpu-h23c5-u1-svn2,cpu-h23c5-u1-svn4,cpu-h23c5-u2-svn1,cpu-h23c5-u2-svn3,cpu-h23c5-u3-svn2,cpu-h23c5-u3-svn4,cpu-h23c5-u4-svn1,cpu-h23c5-u4-svn3,cpu-h23c5-u5-svn2,cpu-h23c5-u5-svn4,cpu-h23c5-u6-svn1,cpu-h23c5-u6-svn3,cpu-h23c5-u7-svn2,cpu-h23c5-u7-svn4,cpu-h23c5-u8-svn1,cpu-h23c5-u8-svn3,cpu-h23c5-u9-svn2,cpu-h23c5-u9-svn4,cpu-h23c5-u10-svn1,cpu-h23c5-u10-svn3,cpu-h23c5-u11-svn2,cpu-h23c5-u11-svn4,cpu-h23c5-u12-svn1,cpu-h23c5-u12-svn3,cpu-h23c5-u13-svn2,cpu-h23c5-u13-svn4,cpu-h23c5-u14-svn1,cpu-h23c5-u14-svn3,cpu-h23c5-u23-svn2,cpu-h23c5-u23-svn4,cpu-h23c5-u24-svn1,cpu-h23c5-u24-svn3,cpu-h23c5-u25-svn2,cpu-h23c5-u25-svn4,cpu-h23c5-u26-svn1,cpu-h23c5-u26-svn3,cpu-h23c5-u27-svn2,cpu-h23c5-u27-svn4,cpu-h23c5-u28-svn1,cpu-h23c5-u28-svn3,cpu-h23c5-u29-svn2,cpu-h23c5-u29-svn4,cpu-h23c5-u30-svn1,cpu-h23c5-u30-svn3,cpu-h23c5-u31-svn2,cpu-h23c5-u31-svn4,cpu-h23c5-u32-svn1,cpu-h23c5-u32-svn3,cpu-h23c5-u33-svn2,cpu-h23c5-u33-svn4,cpu-h23c5-u34-svn1,cpu-h23c5-u34-svn3,cpu-h23c5-u35-svn2,cpu-h23c5-u35-svn4,cpu-h23c5-u36-svn1,cpu-h23c5-u36-svn3,cpu-h23c8-u1-svn2,cpu-h23c8-u1-svn4,cpu-h23c8-u2-svn1,cpu-h23c8-u2-svn3,cpu-h23c8-u3-svn2,cpu-h23c8-u3-svn4,cpu-h23c8-u4-svn1,cpu-h23c8-u4-svn3,cpu-h23c8-u5-svn2,cpu-h23c8-u5-svn4,cpu-h23c8-u6-svn1,cpu-h23c8-u6-svn3,cpu-h23c8-u7-svn2,cpu-h23c8-u7-svn4,cpu-h23c8-u8-svn1,cpu-h23c8-u8-svn3,cpu-h23c8-u9-svn2,cpu-h23c8-u9-svn4,cpu-h23c8-u10-svn1,cpu-h23c8-u10-svn3,cpu-h23c8-u11-svn2,cpu-h23c8-u11-svn4,cpu-h23c8-u12-svn1,cpu-h23c8-u12-svn3,cpu-h23c8-u13-svn2,cpu-h23c8-u13-svn4,cpu-h23c8-u14-svn1,cpu-h23c8-u14-svn3,cpu-h23c8-u23-svn2,cpu-h23c8-u23-svn4,cpu-h23c8-u24-svn1,cpu-h23c8-u24-svn3,cpu-h23c8-u25-svn2,cpu-h23c8-u25-svn4,cpu-h23c8-u26-svn1,cpu-h23c8-u26-svn3,cpu-h23c8-u27-svn2,cpu-h23c8-u27-svn4,cpu-h23c8-u28-svn1,cpu-h23c8-u28-svn3,cpu-h23c8-u29-svn2,cpu-h23c8-u29-svn4,cpu-h23c8-u30-svn1,cpu-h23c8-u30-svn3,cpu-h23c8-u31-svn2,cpu-h23c8-u31-svn4,cpu-h23c8-u32-svn1,cpu-h23c8-u32-svn3,cpu-h23c8-u33-svn2,cpu-h23c8-u33-svn4,cpu-h23c8-u34-svn1,cpu-h23c8-u34-svn3,cpu-h23c8-u35-svn2,cpu-h23c8-u35-svn4,cpu-h23c8-u36-svn1,cpu-h23c8-u36-svn3,cpu-h23d5-u26-sv,cpu-h23d5-u27-sv,cpu-h23d5-u28-sv,cpu-h23d5-u29-sv,cpu-h23d5-u32-sv,cpu-h23d5-u34-sv,cpu-h23d5-u36-sv,cpu-h23d5-u37-svn2,cpu-h23d5-u37-svn4,cpu-h23d5-u38-svn1,cpu-h23d5-u38-svn3,cpu-h24a5-u1-svn2,cpu-h24a5-u1-svn4,cpu-h24a5-u2-svn1,cpu-h24a5-u2-svn3,cpu-h24a5-u3-svn2,cpu-h24a5-u3-svn4,cpu-h24a5-u4-svn1,cpu-h24a5-u4-svn3,cpu-h24a5-u5-svn2,cpu-h24a5-u5-svn4,cpu-h24a5-u6-svn1,cpu-h24a5-u6-svn3,cpu-h24a5-u7-svn2,cpu-h24a5-u7-svn4,cpu-h24a5-u8-svn1,cpu-h24a5-u8-svn3,cpu-h24a5-u9-svn2,cpu-h24a5-u9-svn4,cpu-h24a5-u10-svn1,cpu-h24a5-u10-svn3,cpu-h24a5-u11-svn2,cpu-h24a5-u11-svn4,cpu-h24a5-u12-svn1,cpu-h24a5-u12-svn3,cpu-h24a5-u13-svn2,cpu-h24a5-u13-svn4,cpu-h24a5-u14-svn1,cpu-h24a5-u14-svn3,cpu-h24a5-u23-svn2,cpu-h24a5-u23-svn4,cpu-h24a5-u24-svn1,cpu-h24a5-u24-svn3,cpu-h24a5-u25-svn2,cpu-h24a5-u25-svn4,cpu-h24a5-u26-svn1,cpu-h24a5-u26-svn3,cpu-h24a5-u27-svn2,cpu-h24a5-u27-svn4,cpu-h24a5-u28-svn1,cpu-h24a5-u28-svn3,cpu-h24a5-u29-svn2,cpu-h24a5-u29-svn4,cpu-h24a5-u30-svn1,cpu-h24a5-u30-svn3,cpu-h24a5-u31-svn2,cpu-h24a5-u31-svn4,cpu-h24a5-u32-svn1,cpu-h24a5-u32-svn3,cpu-h24a5-u33-svn2,cpu-h24a5-u33-svn4,cpu-h24a5-u34-svn1,cpu-h24a5-u34-svn3,cpu-h24a5-u35-svn2,cpu-h24a5-u35-svn4,cpu-h24a5-u36-svn1,cpu-h24a5-u36-svn3,cpu-h24b5-u1-svn2,cpu-h24b5-u1-svn4,cpu-h24b5-u2-svn1,cpu-h24b5-u2-svn3,cpu-h24b5-u3-svn2,cpu-h24b5-u3-svn4,cpu-h24b5-u4-svn1,cpu-h24b5-u4-svn3,cpu-h24b5-u5-svn2,cpu-h24b5-u5-svn4,cpu-h24b5-u6-svn1,cpu-h24b5-u6-svn3,cpu-h24b5-u7-svn2,cpu-h24b5-u7-svn4,cpu-h24b5-u8-svn1,cpu-h24b5-u8-svn3,cpu-h24b5-u9-svn2,cpu-h24b5-u9-svn4,cpu-h24b5-u10-svn1,cpu-h24b5-u10-svn3,cpu-h24b5-u11-svn2,cpu-h24b5-u11-svn4,cpu-h24b5-u12-svn1,cpu-h24b5-u12-svn3,cpu-h24b5-u13-svn2,cpu-h24b5-u13-svn4,cpu-h24b5-u14-svn1,cpu-h24b5-u14-svn3,cpu-h24b5-u23-svn2,cpu-h24b5-u23-svn4,cpu-h24b5-u24-svn1,cpu-h24b5-u24-svn3,cpu-h24b5-u25-svn2,cpu-h24b5-u25-svn4,cpu-h24b5-u26-svn1,cpu-h24b5-u26-svn3,cpu-h24b5-u27-svn2,cpu-h24b5-u27-svn4,cpu-h24b5-u28-svn1,cpu-h24b5-u28-svn3,cpu-h24b5-u29-svn2,cpu-h24b5-u29-svn4,cpu-h24b5-u30-svn1,cpu-h24b5-u30-svn3,cpu-h24b5-u31-svn2,cpu-h24b5-u31-svn4,cpu-h24b5-u32-svn1,cpu-h24b5-u32-svn3,cpu-h24b5-u33-svn2,cpu-h24b5-u33-svn4,cpu-h24b5-u34-svn1,cpu-h24b5-u34-svn3,cpu-h24b5-u35-svn2,cpu-h24b5-u35-svn4,cpu-h24b5-u36-svn1,cpu-h24b5-u36-svn3,cpu-h24b8-u1-svn2,cpu-h24b8-u1-svn4,cpu-h24b8-u2-svn1,cpu-h24b8-u2-svn3,cpu-h24b8-u3-svn2,cpu-h24b8-u3-svn4,cpu-h24b8-u4-svn1,cpu-h24b8-u4-svn3,cpu-h24b8-u5-svn2,cpu-h24b8-u5-svn4,cpu-h24b8-u6-svn1,cpu-h24b8-u6-svn3,cpu-h24b8-u7-svn2,cpu-h24b8-u7-svn4,cpu-h24b8-u8-svn1,cpu-h24b8-u8-svn3,cpu-h24b8-u9-svn2,cpu-h24b8-u9-svn4,cpu-h24b8-u10-svn1,cpu-h24b8-u10-svn3,cpu-h24b8-u11-svn2,cpu-h24b8-u11-svn4,cpu-h24b8-u12-svn1,cpu-h24b8-u12-svn3,cpu-h24b8-u13-svn2,cpu-h24b8-u13-svn4,cpu-h24b8-u14-svn1,cpu-h24b8-u14-svn3,cpu-h24b8-u23-svn2,cpu-h24b8-u23-svn4,cpu-h24b8-u24-svn1,cpu-h24b8-u24-svn3,cpu-h24b8-u25-svn2,cpu-h24b8-u25-svn4,cpu-h24b8-u26-svn1,cpu-h24b8-u26-svn3,cpu-h24b8-u27-svn2,cpu-h24b8-u27-svn4,cpu-h24b8-u28-svn1,cpu-h24b8-u28-svn3,cpu-h24b8-u29-svn2,cpu-h24b8-u29-svn4,cpu-h24b8-u30-svn1,cpu-h24b8-u30-svn3,cpu-h24b8-u31-svn2,cpu-h24b8-u31-svn4,cpu-h24b8-u32-svn1,cpu-h24b8-u32-svn3,cpu-h24b8-u33-svn2,cpu-h24b8-u33-svn4,cpu-h24b8-u34-svn1,cpu-h24b8-u34-svn3,cpu-h24b8-u35-svn2,cpu-h24b8-u35-svn4,cpu-h24b8-u36-svn1,cpu-h24b8-u36-svn3,cpu-h24c5-u1-svn2,cpu-h24c5-u1-svn4,cpu-h24c5-u2-svn1,cpu-h24c5-u2-svn3,cpu-h24c5-u3-svn2,cpu-h24c5-u3-svn4,cpu-h24c5-u4-svn1,cpu-h24c5-u4-svn3,cpu-h24c5-u5-svn2,cpu-h24c5-u5-svn4,cpu-h24c5-u6-svn1,cpu-h24c5-u6-svn3,cpu-h24c5-u7-svn2,cpu-h24c5-u7-svn4,cpu-h24c5-u8-svn1,'
        'cpu-h24c5-u8-svn3,cpu-h24c5-u9-svn2,cpu-h24c5-u9-svn4,cpu-h24c5-u10-svn1,cpu-h24c5-u10-svn3,cpu-h24c5-u11-svn2,cpu-h24c5-u11-svn4,cpu-h24c5-u12-svn1,cpu-h24c5-u12-svn3,cpu-h24c5-u13-svn2,cpu-h24c5-u13-svn4,cpu-h24c5-u14-svn1,cpu-h24c5-u14-svn3,cpu-h24c5-u23-svn2,cpu-h24c5-u23-svn4,cpu-h24c5-u24-svn1,cpu-h24c5-u24-svn3,cpu-h24c5-u25-svn2,cpu-h24c5-u25-svn4,cpu-h24c5-u26-svn1,cpu-h24c5-u26-svn3,cpu-h24c5-u27-svn2,cpu-h24c5-u27-svn4,cpu-h24c5-u28-svn1,cpu-h24c5-u28-svn3,cpu-h24c5-u29-svn2,cpu-h24c5-u29-svn4,cpu-h24c5-u30-svn1,cpu-h24c5-u30-svn3,cpu-h24c5-u31-svn2,cpu-h24c5-u31-svn4,cpu-h24c5-u32-svn1,cpu-h24c5-u32-svn3,cpu-h24c5-u33-svn2,cpu-h24c5-u33-svn4,cpu-h24c5-u34-svn1,cpu-h24c5-u34-svn3,cpu-h24c5-u35-svn2,cpu-h24c5-u35-svn4,cpu-h24c5-u36-svn1,cpu-h24c5-u36-svn3,cpu-h24d5-u1-svn2,cpu-h24d5-u1-svn4,cpu-h24d5-u2-svn1,cpu-h24d5-u2-svn3,cpu-h24d5-u3-svn2,cpu-h24d5-u3-svn4,cpu-h24d5-u4-svn1,cpu-h24d5-u4-svn3,cpu-h24d5-u5-svn2,cpu-h24d5-u5-svn4,cpu-h24d5-u6-svn1,cpu-h24d5-u6-svn3,cpu-h24d5-u7-svn2,cpu-h24d5-u7-svn4,cpu-h24d5-u8-svn1,cpu-h24d5-u8-svn3,cpu-h24d5-u9-svn2,cpu-h24d5-u9-svn4,cpu-h24d5-u10-svn1,cpu-h24d5-u10-svn3,cpu-h24d5-u11-svn2,cpu-h24d5-u11-svn4,cpu-h24d5-u12-svn1,cpu-h24d5-u12-svn3,cpu-h24d5-u13-svn2,cpu-h24d5-u13-svn4,cpu-h24d5-u14-svn1,cpu-h24d5-u14-svn3,cpu-h24d5-u23-svn2,cpu-h24d5-u23-svn4,cpu-h24d5-u24-svn1,cpu-h24d5-u24-svn3,cpu-h24d5-u25-svn2,cpu-h24d5-u25-svn4,cpu-h24d5-u26-svn1,cpu-h24d5-u26-svn3,cpu-h24d5-u27-svn2,cpu-h24d5-u27-svn4,cpu-h24d5-u28-svn1,cpu-h24d5-u28-svn3,cpu-h24d5-u29-svn2,cpu-h24d5-u29-svn4,cpu-h24d5-u30-svn1,cpu-h24d5-u30-svn3,cpu-h24d5-u31-svn2,cpu-h24d5-u31-svn4,cpu-h24d5-u32-svn1,cpu-h24d5-u32-svn3,cpu-h24d5-u33-svn2,cpu-h24d5-u33-svn4,cpu-h24d5-u34-svn1,cpu-h24d5-u34-svn3,cpu-h24d5-u35-svn2,cpu-h24d5-u35-svn4,cpu-h24d5-u36-svn1,cpu-h24d5-u36-svn3,cpu-h24d8-u1-svn2,cpu-h24d8-u1-svn4,cpu-h24d8-u2-svn1,cpu-h24d8-u2-svn3,cpu-h24d8-u3-svn2,cpu-h24d8-u3-svn4,cpu-h24d8-u4-svn1,cpu-h24d8-u4-svn3,cpu-h24d8-u5-svn2,cpu-h24d8-u5-svn4,cpu-h24d8-u6-svn1,cpu-h24d8-u6-svn3,cpu-h24d8-u7-svn2,cpu-h24d8-u7-svn4,cpu-h24d8-u8-svn1,cpu-h24d8-u8-svn3,cpu-h24d8-u9-svn2,cpu-h24d8-u9-svn4,cpu-h24d8-u10-svn1,cpu-h24d8-u10-svn3,cpu-h24d8-u11-svn2,cpu-h24d8-u11-svn4,cpu-h24d8-u12-svn1,cpu-h24d8-u12-svn3,cpu-h24d8-u13-svn2,cpu-h24d8-u13-svn4,cpu-h24d8-u14-svn1,cpu-h24d8-u14-svn3,cpu-h24d8-u23-svn2,cpu-h24d8-u23-svn4,cpu-h24d8-u24-svn1,cpu-h24d8-u24-svn3,cpu-h24d8-u25-svn2,cpu-h24d8-u25-svn4,cpu-h24d8-u26-svn1,cpu-h24d8-u26-svn3,cpu-h24d8-u27-svn2,cpu-h24d8-u27-svn4,cpu-h24d8-u28-svn1,cpu-h24d8-u28-svn3,cpu-h24d8-u29-svn2,cpu-h24d8-u29-svn4,cpu-h24d8-u30-svn1,cpu-h24d8-u30-svn3,cpu-h24d8-u31-svn2,cpu-h24d8-u31-svn4,cpu-h24d8-u32-svn1,cpu-h24d8-u32-svn3,cpu-h24d8-u33-svn2,cpu-h24d8-u33-svn4,cpu-h24d8-u34-svn1,cpu-h24d8-u34-svn3,cpu-h24d8-u35-svn2,cpu-h24d8-u35-svn4,cpu-h24d8-u36-svn1,cpu-h24d8-u36-svn3',
        ],
    'max_jobs': 20,
}

site_configuration = {
    'systems': [
        {
            'name': 'um6p',
            'descr': 'Initial build of Toubkal cluster at UM6P: https://www.top500.org/system/179908/',
            'hostnames': ['slurm-control'],
            'modules_system':'lmod',
            'partitions': [
                {
                    **um6p_common,
                    **{
                        'name': 'ib-gcc9-ompi3-ucx',
                        'descr': '100Gb Infiniband using gcc 9.1.0 and openmpi 3.1.6 with UCX',
                        'environs': ['gromacs'],
                        'modules': ['gcc/9.1.0-wq42xr6', 'openmpi/3.1.6-kwhmkxm'],
                        'variables': [
                            ['SLURM_MPI_TYPE', 'pmix_v3'], # available for ompi3+
                            ['UCX_NET_DEVICES', 'mlx5_0:1'], # only use IB
                        ],
                    }
                },
                {
                    **um6p_common,
                    **{
                        'name': 'roce-gcc9-ompi3-ucx',
                        'descr': '50Gb Infiniband using gcc 9.1.0 and openmpi 3.1.6 with UCX',
                        'environs': ['gromacs'],
                        'modules': ['gcc/9.1.0-wq42xr6', 'openmpi/3.1.6-kwhmkxm'],
                        'variables': [
                            ['SLURM_MPI_TYPE', 'pmix_v3'], # available for ompi3+
                            ['UCX_NET_DEVICES', 'mlx5_1:1'], # only use RoCE
                        ],
                    }
                },

            ]
        },
        {
            'name':'csd3',
            'descr': 'Cambridge Service for Data Driven Discovery: https://docs.hpc.cam.ac.uk/hpc/index.html',
            'hostnames': ['login-e-*'],
            'modules_system': 'tmod32',
            'stagedir': '/rds/user/hpcbras1/hpc-work',
            'partitions': [
                {
                    **csd3_cclake_common,
                    **{
                        'name': 'cclake-ib-icc19-impi19-ucx',
                        'descr': '100Gb Infiniband using icc 19.1.2.254 and impi 2019 Update 8 with UCX',
                        'environs': ['sysinfo', 'imb', 'nxnlatbw', 'castep', 'wrf', 'intel-hpl'],
                        'variables': [
                            ['UCX_NET_DEVICES', 'mlx5_0:1'], # only use IB
                        ],
                        'modules': ['rhel7/default-ccl'],
                    },
                },
                {
                    **csd3_cclake_common,
                    **{
                        'name': 'cclake-roce-icc19-impi19-ucx',
                        'descr': '50Gb RoCE using icc 19.1.2.254 and impi 2019 Update 8 with UCX',
                        'environs': ['imb', 'castep', 'wrf', 'nxnlatbw', 'intel-hpl'],
                        'variables': [
                            ['UCX_NET_DEVICES', 'mlx5_1:1'], # only use RoCE
                        ],
                        'modules': ['rhel7/default-ccl'],
                    },
                },
                {
                    **csd3_cclake_common,
                    **{
                        'name': 'cclake-ib-gcc9-ompi3-ucx',
                        'descr': '100Gb Infiniband using gcc 9.1.0 and openmpi 3.1.6 with UCX',
                        'environs': ['imb', 'gromacs', 'omb', 'openfoam', 'nxnlatbw'],
                        'modules': ['openmpi-3.1.6-gcc-9.1.0-omffmfv'],
                        'variables': [
                            ['SLURM_MPI_TYPE', 'pmix_v3'], # available for ompi3+
                            ['UCX_NET_DEVICES', 'mlx5_0:1'], # only use IB
                        ],
                    }
                },
                {
                    **csd3_cclake_common,
                    **{
                        'name': 'cclake-roce-gcc9-ompi3-ucx',
                        'descr': '50Gb Infiniband using gcc 9.1.0 and openmpi 3.1.6 with UCX',
                        'environs': ['imb', 'gromacs', 'omb', 'openfoam', 'nxnlatbw'],
                        'modules': ['openmpi-3.1.6-gcc-9.1.0-omffmfv'],
                        'variables': [
                            ['SLURM_MPI_TYPE', 'pmix_v3'], # available for ompi3+
                            ['UCX_NET_DEVICES', 'mlx5_1:1'], # only use RoCE
                        ],
                    }
                },
                
            ]
        },
        {
            'name':'alaska',
            # Changelist for non-reframe changes:
            # - 10-09-20: C-states disabled
            'descr':'Default AlaSKA OpenHPC p3-appliances slurm cluster',
            'hostnames': ['openhpc-login-0', 'openhpc-compute'],
            'modules_system':'lmod',
            'partitions':[
                {
                    'name':'ib-gcc9-impi-verbs',
                    'descr': '100Gb Infiniband with gcc 9.3.0 and Intel MPI 2019.7.217',
                    'scheduler': 'slurm',
                    'launcher':'mpirun',
                    'max_jobs':8,
                    'environs': ['imb', 'omb', 'intel-hpl', 'intel-hpcg'],
                    'modules': ['gcc/9.3.0-5abm3xg', 'intel-mpi/2019.7.217-bzs5ocr'],
                    'variables': [
                        #['FI_PROVIDER', 'mlx'] # doesn't work, needs ucx
                        ['FI_VERBS_IFACE', 'ib'] # # Network interface to use - this is actually default
                        # these were (failed) attempts to make `srun` work:
                        #['I_MPI_PMI_LIBRARY', '/opt/ohpc/admin/pmix/lib/libpmi.so'], # see https://slurm.schedmd.com/mpi_guide.html#intel_mpi
                        #['SLURM_MPI_TYPE', 'pmi2'],
                    ],
                },
                {
                    'name':'roce-gcc9-impi-verbs',
                    'descr': '25Gb RoCE with gcc 9.3.0 and Intel MPI 2019.7.217 using verbs',
                    'scheduler': 'slurm',
                    'launcher':'mpirun',
                    'max_jobs':8,
                    'environs': ['imb', 'omb', 'intel-hpl', 'intel-hpcg'],
                    'modules': ['gcc/9.3.0-5abm3xg', 'intel-mpi/2019.7.217-bzs5ocr'],
                    'variables': [
                        ['FI_VERBS_IFACE', 'p3p2'] # Network interface to use.
                    ],
                },
                {
                    'name':'ib-gcc9-openmpi4-ucx',
                    'descr':'100Gb Infiniband with gcc 9.3.0 and openmpi 4.0.3 using UCX transport layer',
                    'scheduler': 'slurm',
                    'launcher':'srun',
                    'max_jobs':8,
                    'environs':['imb', 'omb', 'gromacs', 'openfoam', 'cp2k', 'sysinfo', 'nxnlatbw'],
                    'modules': ['gcc/9.3.0-5abm3xg', 'openmpi/4.0.3-qpsxmnc'],
                    'variables': [
                        ['SLURM_MPI_TYPE', 'pmix_v2'],
                        # force IB:
                        ['UCX_NET_DEVICES', 'mlx5_0:1'],
                    ]
                },
                {
                    'name':'roce-gcc9-openmpi4-ucx',
                    'descr':'25Gb RoCE with gcc 9.3.0 and openmpi 4.0.3 using UCX transport layer',
                    'scheduler': 'slurm',
                    'launcher':'srun',
                    'max_jobs':8,
                    'environs':['imb', 'omb', 'gromacs', 'openfoam', 'cp2k', 'nxnlatbw'],
                    'modules': ['gcc/9.3.0-5abm3xg', 'openmpi/4.0.3-qpsxmnc'],
                    'variables': [
                        ['SLURM_MPI_TYPE', 'pmix_v2'],
                        # use roce:
                        ['UCX_NET_DEVICES', 'mlx5_1:1'],
                    ]
                },
            ]
        }, # end alaska
        # < insert new systems here >
    ],
    'environments': [
        {
            'name': 'imb',      # a non-targeted environment seems to be necessary for reframe to load the config
                                # will also work for csd3:cclake-{ib,roce}-icc19-impi19-ucx as the partition's module makes this available
        },
        {
            'name': 'imb',
            'target_systems': ['alaska:ib-gcc9-openmpi4-ucx', 'alaska:roce-gcc9-openmpi4-ucx'],
            'modules': ['intel-mpi-benchmarks/2019.5-dwg5q6j'],
        },
        {
            'name': 'imb',
            'target_systems': ['alaska:ib-gcc9-impi-verbs', 'alaska:roce-gcc9-impi-verbs'],
            'modules': ['intel-mpi-benchmarks/2019.5-w54huiw'],
        },
        {
            'name': 'imb',
            'target_systems': ['csd3:cclake-ib-gcc9-ompi3-ucx', 'csd3:cclake-roce-gcc9-ompi3-ucx'],
            'modules': ['intel-mpi-benchmarks-2019.6-gcc-9.1.0-5tbknir']
        },
        {
            'name': 'gromacs',
        },
        {
            'name': 'gromacs',
            'target_systems': ['um6p:ib-gcc9-ompi3-ucx', 'um6p:roce-gcc9-ompi3-ucx'],
            'modules': ['gromacs/2016.6-rvnthv3']
        },
        {
            'name': 'gromacs',
            'target_systems': ['alaska:ib-gcc9-openmpi4-ucx', 'alaska:roce-gcc9-openmpi4-ucx'],
            'modules': ['gromacs/2016.4-y5sjbs4']
        },
        {
            'name': 'gromacs',
            'target_systems': ['csd3:cclake-ib-gcc9-ompi3-ucx', 'csd3:cclake-roce-gcc9-ompi3-ucx'],
            'modules': ['gromacs-2016.6-gcc-9.1.0-kgomb67']
        },
        {
            'name': 'omb',
        },
        {
            'name': 'omb',
            'target_systems': ['alaska:ib-gcc9-openmpi4-ucx', 'alaska:roce-gcc9-openmpi4-ucx'],
            'modules': ['osu-micro-benchmarks/5.6.2-vx3wtzo']
        },
        {
            'name': 'omb',
            'target_systems': ['alaska:ib-gcc9-impi-verbs', 'alaska:roce-gcc9-impi-verbs'],
            'modules': ['osu-micro-benchmarks/5.6.2-ppxiddg']
        },
        {
            'name': 'omb',
            'target_systems': ['csd3:cclake-ib-gcc9-ompi3-ucx', 'csd3:cclake-roce-gcc9-ompi3-ucx'],
            'modules': ['osu-micro-benchmarks-5.6.3-gcc-9.1.0-nsxydkj']
        },
        {
            'name': 'intel-hpl',
        },
        {
            'name': 'intel-hpl',
            'target_systems': ['alaska:ib-gcc9-impi-verbs', 'alaska:roce-gcc9-impi-verbs'],
            'modules': ['intel-mkl/2020.1.217-5tpgp7b'], # now installed
        },
        {
            'name': 'intel-hpl',
            'target_systems': ['csd3:cclake-ib-icc19-impi19-ucx', 'csd3:cclake-roce-icc19-impi19-ucx'],
            'modules': [], # MKL provided as part of partition's modules
        },
        {
            'name': 'intel-hpcg',
        },
        {
            'name': 'intel-hpcg',
            'target_systems': ['alaska:ib-gcc9-impi-verbs', 'alaska:roce-gcc9-impi-verbs'],
            'modules': ['intel-mkl/2020.1.217-5tpgp7b'],
            'variables':[
                ['PATH', '$PATH:$MKLROOT/benchmarks/hpcg/bin/'], # MKLROOT provided by mkl module
                ['XHPCG_BIN', 'xhpcg_avx2'],
                ['SLURM_CPU_BIND', 'verbose'], # doesn't work as task/affinity plugin not enabled
            ]
        },
        {
            'name':'openfoam'
        },
        {
            'name':'openfoam',
            'target_systems': ['alaska:ib-gcc9-openmpi4-ucx', 'alaska:roce-gcc9-openmpi4-ucx'],
            'modules': ['openfoam-org/7-4zgjbg2']
        },
        {
            'name':'openfoam',
            'target_systems': ['csd3:cclake-ib-gcc9-ompi3-ucx', 'csd3:cclake-roce-gcc9-ompi3-ucx'],
            'modules': ['openfoam-org-7-gcc-9.1.0-dahapws']
        },
        {
            'name':'cp2k',
        },
        {
            'name':'cp2k',
            'target_systems': ['alaska:ib-gcc9-openmpi4-ucx', 'alaska:roce-gcc9-openmpi4-ucx'],
            'modules': ['cp2k/7.1-akb54dx']
        },
        {
            'name': 'sysinfo',
        },
        {
            'name': 'nxnlatbw',
            'cc': 'mpicc',
        },
        {
            'name': 'castep',
        },
        {
            'name': 'castep',
            'target_systems': ['csd3:cclake-ib-icc19-impi19-ucx', 'csd3:cclake-roce-icc19-impi19-ucx'],
            'modules': ['castep'] # castep 17.2.1 with Intel MPI but I don't know which!
        },
        # {
        #     'name': 'sysinfo',
        #     'target_systems': ['alaska:ib-gcc9-openmpi4-ucx'] #, 'alaska:roce-gcc9-openmpi4-ucx'],
        # },
        {
            'name': 'wrf',
        },
        {
            'name': 'wrf',
            'target_systems': ['csd3:cclake-ib-icc19-impi19-ucx', 'csd3:cclake-roce-icc19-impi19-ucx'],
            'modules': [], # intel module already loaded in partition, wrf not defined as module (yet)
            'variables': [['WRF_DIR', "$HOME/wrf-build-icc19-impi19-hsw/WRFV3.8.1"]] # TODO: use a module instead
        },
    ],
    'logging': [
        {
            'level': 'debug',
            'handlers': [
                {
                    'type': 'file',
                    'name': 'reframe.log',
                    'level': 'debug',
                    'format': '[%(asctime)s] %(levelname)s: %(check_name)s: %(message)s',   # noqa: E501
                    'append': False
                },
                {
                    'type': 'stream',
                    'name': 'stdout',
                    'level': 'info',
                    'format': '%(message)s'
                },
                {
                    'type': 'file',
                    'name': 'reframe.out',
                    'level': 'info',
                    'format': '%(message)s',
                    'append': False
                }
            ],
            'handlers_perflog': [
                {
                    'type': 'filelog',
                    # make this the same as output filenames which are ('sysname', 'partition', 'environ', 'testname', 'filename')
                    'prefix': '%(check_system)s/%(check_partition)s/%(check_environ)s/%(check_name)s', # <testname>.log gets appended
                    'level': 'info',
                    # added units here - see Reference: https://reframe-hpc.readthedocs.io/en/latest/config_reference.html?highlight=perflog#logging-.handlers_perflog
                    'format': '%(check_job_completion_time)s|reframe %(version)s|%(check_info)s|jobid=%(check_jobid)s|%(check_perf_var)s=%(check_perf_value)s|%(check_perf_unit)s|ref=%(check_perf_ref)s (l=%(check_perf_lower_thres)s, u=%(check_perf_upper_thres)s)|%(check_tags)s',  # noqa: E501
                    'datefmt': '%FT%T%:z',
                    'append': True
                }
            ]
        }
    ],
    'general': [
        {
            'check_search_path': ['./'],
            'check_search_recursive': True
        }
    ]    
}
