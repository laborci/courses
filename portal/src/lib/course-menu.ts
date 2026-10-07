import type { NavItem } from '../../scripts/content';

export function courseMenu(items: NavItem[], currentSlug: string, courseSlug: string) {
  const current = items.find(item => item.slug === currentSlug) || items.find(item => item.slug === courseSlug);
  if (!current) return { parent: null, items: [] as NavItem[] };
  const children = items.filter(item => item.parent === current.slug);
  const parent = children.length || current.slug === courseSlug
    ? current
    : items.find(item => item.slug === current.parent) || current;
  return { parent, items: items.filter(item => item.parent === parent.slug) };
}
