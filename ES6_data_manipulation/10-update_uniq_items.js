export default function updateUniqueItems(grocery) {
  if (grocery instanceof Map) {
    for (const [key, value] of grocery.entries()) {
      if (value === 1) {
        grocery.set(key, 100);
      }
    }
  } else {
    throw new Error('Cannot process');
  }
  return grocery;
}
