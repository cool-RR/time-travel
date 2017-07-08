"""A patch to the time module."""

import mock


class TimePatcher(object):
    """Context-manager patching the time module.
    
    Patching:
        - time
    """
    
    def __init__(self, clock):
        """Create the patch.
        
        @start_time is time in seconds since the epoch.
        """
        self.clock = clock
        
        self.patches = [mock.patch('time.time',
                                   side_effect=self.clock.get_timestamp),
                        mock.patch('time.sleep',
                                   side_effect=self.clock.advance_timestamp),
                        ]
    
#     def advance_time(self, secs):
#         """Increase the returned time in a given amount of seconds."""
#         self.clock.advance_time(secs)
        
    def start(self):
        """Start mocking time module."""
        for p in self.patches:
            p.start()
            
    def stop(self):
        """Stop mocking time module."""
        for p in self.patches:
                p.stop()
                
    def __enter__(self):
        self.start()
        return self
        
    def __exit__(self, *args):
        self.stop()
