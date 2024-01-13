// Schema:
// date, Host A, Host B, Host C
const networkData = [
  [1, 120, 80, 100],
  [2, 150, 90, 120],
  [3, 110, 70, 80],
  [4, 130, 100, 110],
  [5, 90, 60, 70],
  [6, 180, 120, 160],
  [7, 160, 110, 140],
  [8, 170, 130, 150],
  [9, 220, 180, 200],
  [10, 200, 160, 180],
  [11, 110, 70, 80],
  [12, 120, 90, 100],
  [13, 140, 110, 130],
  [14, 200, 150, 180],
  [15, 180, 140, 160],
  [16, 130, 60, 110],
  [17, 170, 120, 150],
  [18, 220, 190, 200],
  [19, 130, 80, 120],
  [20, 80, 40, 70],
  [21, 110, 50, 90],
  [22, 170, 140, 160],
  [23, 190, 150, 180],
  [24, 100, 60, 110],
  [25, 120, 70, 100],
  [26, 160, 130, 140],
  [27, 240, 200, 220],
  [28, 170, 140, 160],
  [29, 150, 120, 130],
  [30, 100, 50, 70],
  [31, 90, 10, 60]
];

var schema = [
  { name: 'date', index: 0, text: '日期' },
  { name: 'HostA', index: 1, text: '主机A' },
  { name: 'HostB', index: 2, text: '主机B' },
  { name: 'HostC', index: 3, text: '主机C' }
];
var lineStyle = {
  width: 1,
  opacity: 0.5
};

option = {
  backgroundColor: '#333',
  legend: {
    bottom: 30,
    data: ['Host A', 'Host B', 'Host C'],
    itemGap: 20,
    textStyle: {
      color: '#fff',
      fontSize: 14
    }
  },
  tooltip: {
    padding: 10,
    backgroundColor: '#222',
    borderColor: '#777',
    borderWidth: 1
  },
  parallelAxis: [
    {
      dim: 0,
      name: schema[0].text,
      inverse: true,
      max: 31,
      nameLocation: 'start'
    },
    { dim: 1, name: schema[1].text },
    { dim: 2, name: schema[2].text },
    { dim: 3, name: schema[3].text }
  ],
  visualMap: {
    show: true,
    min: 0,
    max: 250,
    dimension: 2,
    inRange: {
      color: ['#d94e5d', '#eac736', '#50a3ba'].reverse()
    }
  },
  parallel: {
    left: '5%',
    right: '18%',
    bottom: 100,
    parallelAxisDefault: {
      type: 'value',
      name: '流量指数',
      nameLocation: 'end',
      nameGap: 20,
      nameTextStyle: {
        color: '#fff',
        fontSize: 12
      },
      axisLine: {
        lineStyle: {
          color: '#aaa'
        }
      },
      axisTick: {
        lineStyle: {
          color: '#777'
        }
      },
      splitLine: {
        show: false
      },
      axisLabel: {
        color: '#fff'
      }
    }
  },
  series: [
    {
      name: 'Host A',
      type: 'parallel',
      lineStyle: lineStyle,
      data: networkData
    },
    {
      name: 'Host B',
      type: 'parallel',
      lineStyle: lineStyle,
      data: networkData
    },
    {
      name: 'Host C',
      type: 'parallel',
      lineStyle: lineStyle,
      data: networkData
    }
  ]
};

option && myChart.setOption(option);
