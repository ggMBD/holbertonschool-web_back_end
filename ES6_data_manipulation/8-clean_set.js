export default function cleanSet(set, startString) {
  if (startString === '' || typeof startsString !== 'string') {
    return '';
  }
  const result = [];
  result.forEach((value) => {
    if (value.startsWith(startString)) {
      result.push(value.slice(startString.length));
    }
  });
  return result.join('-');
}
