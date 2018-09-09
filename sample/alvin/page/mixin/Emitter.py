# 事件处理器
class Emitter(object):
    def __init__(self):
        super(Emitter, self).__init__()
        self.event_stack = {}

    def on(self, event_name, callback):
        """
        事件绑定方法
          :param self:
          :param event_name: 事件名称
          :param callback: callable对象，回调方法
        """
        if not callable(callback):
            return self
        event_stack = getattr(self, 'event_stack', {})
        event = event_stack.get(event_name, [])
        event.append(callback)
        event_stack[event_name] = event
        self.event_stack = event_stack
        return self

    def off(self, event_name, callback):
        """
        解除事件绑定
          :param self:
          :param event_name: 事件名
          :param callback: 绑定时的回调方法
        """
        event_stack = getattr(self, 'event_stack', {})
        if callback:
            if event_stack.get(event_name, None):
                event_stack[event_name].remove(callback)
        else:
            event_stack[event_name] = None
        self.event_stack = event_stack
        return self

    def _emit(self, event_name, data):
        """
        触发事件
          :param self:
          :param event_name: 事件名
          :param data: 事件数据
        """
        event_stack = getattr(self, 'event_stack', {})
        if event_stack.get(event_name, None):
            for callback in self.event_stack.get(event_name, []):
                callback({'name': event_name, 'data': data, 'target': self})
